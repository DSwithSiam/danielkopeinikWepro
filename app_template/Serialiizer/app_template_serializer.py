from rest_framework import serializers 


# uploaded  related serializer and template model 

from app_template.Model.app_template_model import AppTemplateModel

from accounts.serializers import GetUserSerializer
from app_template.Serialiizer.template_image_serializer import TemplateImageSerializer
from app_template.Model.template_image_model import TemplateImageModel


# create serializer for AppTemplateModel 


class CreateAppTemplateSerializer(serializers.ModelSerializer):
    
    template_images= TemplateImageSerializer(read_only=True,many=False,required=False)

    image_titles= serializers.ListField(
        child= serializers.CharField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = AppTemplateModel
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    

    def create(self,validated_data):
        images= validated_data.pop('template_images',[])
        titles = validated_data.pop('image_titles',[])

        app_template = AppTemplateModel.objects.create(**validated_data)


        for index, image in enumerate(images):
            title = titles[index] if index < len(titles) else None
            TemplateImageModel.objects.create(
                template=app_template,
                image=image,
                image_title=title
            )

            
        return app_template





class GetAppTemplateSerializer(serializers.ModelSerializer):

    user = GetUserSerializer(read_only=True) 

    

    class Meta:

        model = AppTemplateModel
        fields = '__all__'
       



