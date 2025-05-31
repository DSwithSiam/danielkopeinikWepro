from rest_framework import serializers 

from app_template.Model.template_image_model import TemplateImageModel

from code_snippet.image_casting import Base64ImageField



class TemplateImageSerializer(serializers.ModelSerializer):

    # image=Base64ImageField()
    class Meta:
        model = TemplateImageModel
        fields = ['image', 'image_title']






class GetTemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateImageModel
        fields = ['image', 'image_title']