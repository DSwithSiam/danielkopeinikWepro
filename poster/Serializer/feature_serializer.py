from  rest_framework import serializers 

from poster.Model.feature_model  import FeatureBasePriceModel



class FetureBasePriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeatureBasePriceModel 
        fields = '__all__'
