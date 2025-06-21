from rest_framework import serializers 


from poster.Model.brand_model import BrandModel 

from accounts.serializers import GetUserSerializer 


class BrandSerializer(serializers.ModelSerializer):

    class Meta:

        model = BrandModel
        fields = '__all__'


    





class GetBrandSerializer(serializers.ModelSerializer):


    customer = GetUserSerializer(read_only=True,many=False)

    class Meta:

        model = BrandModel
        fields = '__all__'


        