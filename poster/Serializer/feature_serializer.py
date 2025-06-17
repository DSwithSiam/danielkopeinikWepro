from  rest_framework import serializers 

from poster.Model.feature_model  import FeatureBasePriceModel



class FetureBasePriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeatureBasePriceModel 
        fields = '__all__'



class FeaturePriceCalculationSerializer(serializers.Serializer):
    posting_generation = serializers.IntegerField(default=0)
    custom_app = serializers.IntegerField(default=0)
    ai_inclusion =serializers.IntegerField(default=0)
    custom_design_inclusion = serializers.IntegerField(default=0)
    color_design_inclusion = serializers.IntegerField(default=0)
    logo_design_inclusion = serializers.IntegerField(default=0)
    we_pro_branding = serializers.IntegerField(default=0)


    