from rest_framework.viewsets  import ModelViewSet 

from app_template.Model.template_image_model import TemplateImageModel 

from app_template.Serialiizer.template_image_serializer import (

    TemplateImageSerializer,
    GetTemplateImageSerializer
)


class TemplateImageModelViewSet(ModelViewSet):
 
    queryset = TemplateImageModel.objects.select_related('template')

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update','destroy']:
            return   TemplateImageSerializer
        
        else:
            return GetTemplateImageSerializer