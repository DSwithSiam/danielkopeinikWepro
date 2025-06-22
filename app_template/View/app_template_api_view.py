from  rest_framework.viewsets import ModelViewSet 


# import related serializers and models 

from app_template.Serialiizer.app_template_serializer import (
    CreateAppTemplateSerializer,
    GetAppTemplateSerializer,
    UpdateAppTemplateSerializer
)

from app_template.Model.app_template_model import AppTemplateModel 

from app_template.custom_permission import IsAdminOrOwner
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action 
from rest_framework.response import Response 
from rest_framework import status 



class AppTemplateModelViewSet(ModelViewSet):
    """
    Viewset for AppTemplateModel.
    Provides create, retrieve, update, and delete functionality.
    """
    queryset = AppTemplateModel.objects.select_related('user')
    # serializer_class = GetAppTemplateSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]
    permission_classes= [IsAuthenticated]


    # permission_classes = [IsAdminOrOwner]  # Custom permission to restrict access based on user role and ownership
    # create_serializer_class = CreateAppTemplateSerializer   


    def get_serializer_class(self):


        if self.action in ['create',  'destroy']:
            return CreateAppTemplateSerializer
        
        elif self.action  in ['update','partial-update']:
            return UpdateAppTemplateSerializer
        else:
            return GetAppTemplateSerializer 
        
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user) 



    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.query_params.get('title', None) 

        if title:
            queryset = queryset.filter(title__icontains=title)

        queryset = queryset.order_by('-created_at')  # Order by created_at in descending order 

        return queryset 
    
    @action(detail=False, methods=['get'], url_path='latest')
    def latest_app_template(self, request):
        latest_template = AppTemplateModel.objects.filter(user=request.user).order_by('-created_at').first()
        if latest_template:
            serializer = self.get_serializer(latest_template)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'No app template found.'}, status=status.HTTP_404_NOT_FOUND)
    
    # this return only auth user based template 
    @action(detail=False,methods=['get'],url_path='auth/only')
    def auth_user_based_template(self,request):

        auth_user_app = AppTemplateModel.objects.filter(user=request.user)

        if auth_user_app:

            serializer = self.get_serializer(auth_user_app)

            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(
            {
                'error':'not created any app yet, please create!!'
            },
            status=status.HTTP_400_OK
        )

    


    

        













    