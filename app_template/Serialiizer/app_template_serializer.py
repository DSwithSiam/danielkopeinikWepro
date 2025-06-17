from rest_framework import serializers 


# uploaded  related serializer and template model 

from app_template.Model.app_template_model import AppTemplateModel

from accounts.serializers import GetUserSerializer
from app_template.Serialiizer.template_image_serializer import TemplateImageSerializer
from app_template.Model.template_image_model import TemplateImageModel

from poster.Model.membership_model  import MemberShipPlan


from  code_snippet.stripe_user_checkup import has_active_subscription 



class CreateAppTemplateSerializer(serializers.ModelSerializer):
    template_images = TemplateImageSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = AppTemplateModel
        fields = '__all__'



    def validate(self,attrs):

        request = self.context.get('request')
        auth_user = request.user 

        # Step 1: Check Stripe subscription

        is_subscribe,message = has_active_subscription(auth_user.email)

        if not is_subscribe:
            raise serializers.ValidationError(f"You are not subscribed: {message}")
        
        # Step 2: Get current app template count

        existing_count = AppTemplateModel.objects.filter(user=auth_user).count() or 0 

        # Step 3: Get latest successful subscription plan

        try:

            membership=MemberShipPlan.objects.filter(
                customer=auth_user
            ).latest('created_at')

            allowed_limit = int(membership.custom_app) 


            if existing_count >= allowed_limit:
                raise serializers.ValidationError('You have already exceeds the limit')
            
            return attrs 
            
        except   MemberShipPlan.DoesNotExist:
            raise serializers.ValidationError("No active membership plan found.")



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

    

    class Meta:

        model = AppTemplateModel
        fields = '__all__'
       






class UpdateAppTemplateSerializer(serializers.ModelSerializer):
    # template_images = TemplateImageSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = AppTemplateModel
        fields = '__all__'
