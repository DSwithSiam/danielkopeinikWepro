from rest_framework.viewsets import ModelViewSet 

from poster.Model.brand_model import BrandModel 
from poster.Serializer.brand_serializer import (

BrandSerializer,
GetBrandSerializer

)


from rest_framework.permissions import IsAuthenticated,IsAdminUser


class BrandModelViewSet(ModelViewSet):

    # queryset = BrandModel.objects.select_related('customer').filter(customer=self.request.user)
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None 


    def get_serializer_class(self):

        if self.action in ('create','update','partial_update','destroy'):
            return BrandSerializer
        
        return GetBrandSerializer
    

    def perform_create(self,serializer):

        serializer.save(customer = self.request.user)

    def get_queryset(self):

        return BrandModel.objects.select_related('customer').filter(customer = self.request.user)



