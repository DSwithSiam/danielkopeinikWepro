from rest_framework import serializers 

from app_template.Model.template_image_model import TemplateImageModel




class TemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateImageModel
        fields = ['image', 'image_title']






class GetTemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateImageModel
        fields = ['image', 'image_title']