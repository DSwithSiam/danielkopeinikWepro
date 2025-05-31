from rest_framework.viewsets import ModelViewSet 

from app_template.Model.product_model import ProductModel 

from app_template.Serialiizer.product_serializer import (

    CreateProductSerializer,
    GetProductSerializer
)


from rest_framework.permissions import IsAuthenticated 



class ProductModelViewSet(ModelViewSet):

    queryset=ProductModel.objects.select_related('template')

    def get_serializer_class(self):
        
        if self.action in  ['create','update','partial_update','destroy']:
            return CreateProductSerializer
        
        return GetProductSerializer
    
    