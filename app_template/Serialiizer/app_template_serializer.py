from rest_framework import serializers 


# uploaded  related serializer and template model 

from app_template.Model.app_template_model import AppTemplateModel

from accounts.serializers import GetUserSerializer
from app_template.Serialiizer.template_image_serializer import TemplateImageSerializer
from app_template.Model.template_image_model import TemplateImageModel

from poster.Model.membership_model  import MemberShipPlan

from app_template.Model.app_visit_model import AppVisitModel

from poster.Serializer.brand_serializer import OnlyBrandSerializer 
from poster.Model.brand_model import BrandModel 

from  code_snippet.stripe_user_checkup import has_active_subscription 


# from app_template.Serialiizer.product_serializer import OnlyProductSerializer



class CreateAppTemplateSerializer(serializers.ModelSerializer):
    template_images = TemplateImageSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = AppTemplateModel
        exclude =['user']


    def create(self, validated_data):
      
        template_images_data = validated_data.pop('template_images', [])

        print(template_images_data)

        request = self.context.get('request')
        index = 0
        while True:
            image_file = request.FILES.get(f'template_images[{index}][image]')
            image_title = request.data.get(f'template_images[{index}][image_title]')
            if not image_file and not image_title:
                break
            template_images_data.append({
                'image': image_file,
                'image_title': image_title
            })
            index += 1

        app_template = AppTemplateModel.objects.create(**validated_data)

        for image_data in template_images_data:
            TemplateImageModel.objects.create(template=app_template, **image_data)

        return app_template



class GetAppTemplateSerializer(serializers.ModelSerializer):

    user = GetUserSerializer(read_only=True) 
    app_visit_count = serializers.SerializerMethodField()
    brand= serializers.SerializerMethodField()

    
    class Meta:

        model = AppTemplateModel
        fields = '__all__'

    def get_app_visit_count(self,obj):

        request = self.context.get('request',None)

        if request and request.user.is_authenticated :

            return AppVisitModel.objects.filter(
                template=obj,
                user = request.user
            ).count()
        
        return 0 
    
    def get_brand(self, obj):

        try:
            brand = obj.user.brand_author
            request = self.context.get('request')  # ✅ forward context

            return OnlyBrandSerializer(brand, context={'request': request}).data
        except BrandModel.DoesNotExist:
            return None





# This serializer used only for updating 

class UpdateAppTemplateSerializer(serializers.ModelSerializer):
    # template_images = TemplateImageSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = AppTemplateModel
        fields = '__all__'



# This Serializer used for overall app template serializer where brand,products for price_lists , additional_image for other app user 

class OverallAppTemplateSerializer(serializers.ModelSerializer):

    user = GetUserSerializer(read_only=True) 
    brand= serializers.SerializerMethodField()
    products= serializers.SerializerMethodField()
    extra_images= serializers.SerializerMethodField()

    

    class Meta:

        model = AppTemplateModel
        fields = '__all__'

    
     
    # def get_brand(self,obj):

    #     try:
    #         brand = obj.user.brand_author
    #         return  OnlyBrandSerializer(brand).data 
        
    #     except BrandModel.DoesNotExist:
    #         return None 

    def get_brand(self, obj):
        
        try:
            brand = obj.user.brand_author
            request = self.context.get('request') 

            return OnlyBrandSerializer(brand, context={'request': request}).data
        except BrandModel.DoesNotExist:
            return None

    def get_products(self,obj):
        from app_template.Serialiizer.product_serializer import OnlyProductSerializer
        products= obj.product_template.all()
        request= self.context.get('request')


        return OnlyProductSerializer(products,many=True,context={'request': request}).data 
    
    def get_extra_images(self,obj):

        from app_template.Serialiizer.template_image_serializer import TemplateImageSerializer

        extra_images= obj.template_images.all()
        request = self.context.get('request')

        return TemplateImageSerializer(extra_images,many=True,context={'request':request}).data 
    
    
        


