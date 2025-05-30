from rest_framework import serializers 


# uploaded  related serializer and template model 

from app_template.Model.app_template_model import AppTemplateModel

from accounts.serializers import GetUserSerializer


from app_template.Serialiizer.template_image_serializer import TemplateImageSerializer

from app_template.Model.app_template_model import TemplateImageModel

# create serializer for AppTemplateModel 


class CreateAppTemplateSerializer(serializers.ModelSerializer):
    additional_image = TemplateImageSerializer(write_only=True, many=True, required=False)
    
    class Meta:
        model = AppTemplateModel
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        additional_images_data = validated_data.pop('additional_image', [])
        app_template = AppTemplateModel.objects.create(**validated_data)
        
        for image_data in additional_images_data:
            image_instance = TemplateImageModel.objects.create(**image_data)
            app_template.additional_image.add(image_instance)
        
        return app_template





class GetAppTemplateSerializer(serializers.ModelSerializer):

    user = GetUserSerializer(read_only=True) 

    additional_image= TemplateImageSerializer(read_only=True,many=True)

    class Meta:

        model = AppTemplateModel
        fields = '__all__'
       



