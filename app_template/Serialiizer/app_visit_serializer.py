from rest_framework import serializers 

# import related model and serializer 

from app_template.Model.app_visit_model import AppVisitModel 
from  app_template.Serialiizer.app_template_serializer import GetAppTemplateSerializer 



class CreateAppVisitSerializer(serializers.ModelSerializer):

    class Meta:

        model = AppVisitModel
        exclude = ['user']





class GetAppVisitSerializer(serializers.ModelSerializer):

    template = GetAppTemplateSerializer(read_only=True,many = False)

    class Meta:

        model = AppVisitModel
        exclude = ['user']