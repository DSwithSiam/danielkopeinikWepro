from rest_framework.viewsets import ModelViewSet 


# import serailizer and model 

from poster.Model.feature_model  import FeatureBasePriceModel 

from poster.Serializer.feature_serializer  import FetureBasePriceSerializer

from rest_framework.permissions import IsAuthenticated,IsAdminUser




class FetureBasePriceModelViewSet(ModelViewSet):

    queryset = FeatureBasePriceModel.objects.all().order_by('-id') 
    serializer_class = FetureBasePriceSerializer
    permission_class = [IsAuthenticated]

