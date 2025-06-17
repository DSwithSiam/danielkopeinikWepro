from rest_framework.viewsets import ModelViewSet 


# import serailizer and model 

from poster.Model.feature_model  import FeatureBasePriceModel 

from poster.Serializer.feature_serializer  import (
    
    FetureBasePriceSerializer,
    FeaturePriceCalculationSerializer

)

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 

from rest_framework.decorators import action




class FetureBasePriceModelViewSet(ModelViewSet):

    queryset = FeatureBasePriceModel.objects.all().order_by('-id') 
    serializer_class = FetureBasePriceSerializer
    permission_class = [IsAuthenticated]


    
    @action(detail=False, methods=['post'], url_path='custom/price')
    def CustomEnterprisePrice(self,request):

        serializer= FeaturePriceCalculationSerializer(data = request.data)

        if serializer.is_valid():

            data = serializer.validated_data 
            base_price = FeatureBasePriceModel.objects.first()

            if not base_price:
                return Response({'error':'admin  not set up base price yet,try agian please'},status = status.HTTP_400_BAD_REQUEST)
            
            # Cumulative Price Set Up for custom Subscription user 

            cumulative_price =0 

            cumulative_price+= base_price.posting_generation* data['posting_generation']
            cumulative_price+= base_price.custom_app* data['custom_app']
            cumulative_price+= base_price.ai_inclusion* data['ai_inclusion']
            cumulative_price+= base_price.custom_design_inclusion* data['custom_design_inclusion']
            cumulative_price+= base_price.color_design_inclusion* data['color_design_inclusion']
            cumulative_price+= base_price.logo_design_inclusion* data['logo_design_inclusion']
            cumulative_price+= base_price.we_pro_branding* data['we_pro_branding']

            return Response({
                'total_price': round(cumulative_price, 2)
            },
            status = status.HTTP_200_OK
            )


            



class FeatureCumulativePriceAPIVIew(APIView):

    permission_classes = [IsAuthenticated]


    def post(self,request,*args,**kwargs):

        serializer= FeaturePriceCalculationSerializer(data = request.data)

        if serializer.is_valid():

            data = serializer.validated_data

            base_price = FeatureBasePriceModel.objects.first()

            if not base_price:
                return Response({'error':'Base Price Not Configured'},status = status.HTTP_400_BAD_REQUEST)
            
            
            # cumulative price for custom subscription user 

            cumulative_price = 0 

            cumulative_price+= base_price.posting_generation* data['posting_generation']
            cumulative_price+= base_price.custom_app* data['custom_app']
            cumulative_price+= base_price.ai_inclusion* data['ai_inclusion']
            cumulative_price+= base_price.custom_design_inclusion* data['custom_design_inclusion']
            cumulative_price+= base_price.color_design_inclusion* data['color_design_inclusion']
            cumulative_price+= base_price.logo_design_inclusion* data['logo_design_inclusion']
            cumulative_price+= base_price.we_pro_branding* data['we_pro_branding']

            return Response({
                'total_price': round(cumulative_price, 2)
            },
            status = status.HTTP_200_OK
            )









            










