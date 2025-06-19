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
    
    

        













    