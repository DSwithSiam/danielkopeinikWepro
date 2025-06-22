from  rest_framework import serializers 

from poster.Model.poster_model import  PosterModel 

from app_template.Serialiizer.app_template_serializer import GetAppTemplateSerializer 
from app_template.Model.app_template_model  import AppTemplateModel 



class CreatePosterSerializer(serializers.ModelSerializer):

    app_template= serializers.PrimaryKeyRelatedField(queryset=AppTemplateModel.objects.all(),many=False)
    class Meta:

        model  = PosterModel
        fields = '__all__'




class GetPosterModelSerializer(serializers.ModelSerializer):

    app_template= GetAppTemplateSerializer(read_only= True , many=False,required=False)

    class Meta:
        model = PosterModel
        fields ='__all__'

