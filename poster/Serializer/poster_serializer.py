from  rest_framework import serializers 

from poster.Model.poster_model import  PosterModel 

from app_template.Serialiizer.app_template_serializer import GetAppTemplateSerializer 




class CreatePosterSerializer(serializers.ModelSerializer):

    class Meta:

        model  = PosterModel
        fields = '__all__'




class GetPosterModelSerializer(serializers.ModelSerializer):

    app_template= GetAppTemplateSerializer(read_only= True , many=False,required=False)

    class Meta:
        model = PosterModel
        fields ='__all__'

