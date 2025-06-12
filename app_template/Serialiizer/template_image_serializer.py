from rest_framework import serializers 

from app_template.Model.template_image_model import TemplateImageModel

from code_snippet.image_casting import Base64ImageField

# from app_template.Serialiizer.app_template_serializer  import GetAppTemplateSerializer

class TemplateImageSerializer(serializers.ModelSerializer):

    # image=Base64ImageField()
    class Meta:
        model = TemplateImageModel
        fields = ['image', 'image_title']




<<<<<<< HEAD

<<<<<<< HEAD

class GetTemplateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateImageModel
        fields = ['id','image', 'image_title']






=======
=======
class GetTemplateImageSerializer(serializers.ModelSerializer):

    # template=GetAppTemplateSerializer(read_only=True,many=False)
    class Meta:
        model = TemplateImageModel
        fields = ['image', 'image_title']
>>>>>>> origin/feature_rahim
>>>>>>> d783ca335dd59c020b82c76c5fa9c377bad83a7a
