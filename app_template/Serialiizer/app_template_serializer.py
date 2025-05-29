from rest_framework import serializers 


# uploaded  related serializer and template model 

from app_template.Model.app_template_model import AppTemplateModel

from accounts.serializers import GetUserSerializer


# create serializer for AppTemplateModel 

class   CreateAppTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppTemplateModel
        exclude = ['user']
        read_only_fields = ['created_at', 'updated_at']

# Get Serializer for AppTemplateModel 



class GetAppTemplateSerializer(serializers.ModelSerializer):

    user = GetUserSerializer(read_only=True) 


    class Meta:

        model = AppTemplateModel
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'user']




