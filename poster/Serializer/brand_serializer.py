from rest_framework import serializers 


from poster.Model.brand_model import BrandModel 

class BrandSerializer(serializers.ModelSerializer):

    class Meta:

        model = BrandModel
        fields = '__all__'