from rest_framework.viewsets import ModelViewSet 

from app_template.Model.product_model import ProductModel 

from app_template.Serialiizer.product_serializer import (

    CreateProductSerializer,
    GetProductSerializer
)


from rest_framework.permissions import IsAuthenticated 

from  rest_framework.decorators import action 
from rest_framework.response import Response 
from rest_framework import status 



class ProductModelViewSet(ModelViewSet):

    queryset=ProductModel.objects.select_related('template')

    def get_serializer_class(self):
        
        if self.action in  ['create','update','partial_update','destroy']:
            return CreateProductSerializer
        
        return GetProductSerializer
    

    @action(detail=False,methods=['get'],url_path='user_product')
    def user_price_list_product(self,request):

        # Here I only target to price list template to related user 

        price_list_product = ProductModel.objects.filter(template__app_category='prices_lists',template__user=request.user)

        if price_list_product.exists():
            serializer = self.get_serializer(price_list_product,many=True)

            return Response(serializer.data,status=status.HTTP_200_OK)
        

        return Response({'error':'No related product model found'},status=status.HTTP_404_NOT_FOUND)
    
    