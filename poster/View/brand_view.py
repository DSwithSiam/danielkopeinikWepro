from rest_framework.viewsets import ModelViewSet 

from poster.Model.brand_model import BrandModel 
from poster.Serializer.brand_serializer import BrandSerializer 


from rest_framework.permissions import IsAuthenticated,IsAdminUser


class BrandModelViewSet(ModelViewSet):

    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = [IsAuthenticated]


