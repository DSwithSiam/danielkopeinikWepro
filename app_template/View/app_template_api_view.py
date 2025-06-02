from  rest_framework.viewsets import ModelViewSet 


# import related serializers and models 

from app_template.Serialiizer.app_template_serializer import (
    CreateAppTemplateSerializer,
    GetAppTemplateSerializer
)

from app_template.Model.app_template_model import AppTemplateModel 

from app_template.custom_permission import IsAdminOrOwner
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser



class AppTemplateModelViewSet(ModelViewSet):
    """
    Viewset for AppTemplateModel.
    Provides create, retrieve, update, and delete functionality.
    """
    queryset = AppTemplateModel.objects.select_related('user')
    serializer_class = GetAppTemplateSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]


    # permission_classes = [IsAdminOrOwner]  # Custom permission to restrict access based on user role and ownership
    # create_serializer_class = CreateAppTemplateSerializer   


    def get_serializer_class(self):


        if self.action in ['create', 'update', 'partial_update','destroy']:
            return CreateAppTemplateSerializer
        
        return GetAppTemplateSerializer 



    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.query_params.get('title', None) 

        if title:
            queryset = queryset.filter(title__icontains=title)

        queryset = queryset.order_by('-created_at')  # Order by created_at in descending order 

        return queryset 
    
    

        













    