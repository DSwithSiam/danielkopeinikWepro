from app_template.Model.app_template_model import AppTemplateModel 

from rest_framework import serializers 

from app_template.Serialiizer.app_template_serializer import GetAppTemplateSerializer 
from app_template.Model.product_model import ProductModel 


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductModel

        fields = '__all__'




class GetProductSerializer(serializers.ModelSerializer):

    template = GetAppTemplateSerializer(read_only = True, many=False)

    class Meta:

        model = ProductModel

        fields = "__all__"






class OnlyProductSerializer(serializers.ModelSerializer):

   
    class Meta:

        model = ProductModel

        exclude =['template']


