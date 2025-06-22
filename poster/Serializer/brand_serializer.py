from rest_framework import serializers 


from poster.Model.brand_model import BrandModel 

from accounts.serializers import GetUserSerializer 


class BrandSerializer(serializers.ModelSerializer):

    class Meta:

        model = BrandModel
        fields = '__all__'


    





class GetBrandSerializer(serializers.ModelSerializer):


    customer = GetUserSerializer(read_only=True,many=False)

    class Meta:

        model = BrandModel
        fields = '__all__'



# only for using main app website 






# class OnlyBrandSerializer(serializers.ModelSerializer):

    
#     class Meta:

#         model = BrandModel
#         exclude = ['customer']

class OnlyBrandSerializer(serializers.ModelSerializer):
    company_logo = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = BrandModel
        fields = [
            'id', 'company_name', 'company_logo', 'profile_picture',
            'facebook_link', 'instagram_link', 'twiter_link', 'linkedin_link',
            'hotel_website_link', 'profile_name', 'hotel_location',
            'main_color', 'background_color', 'heading_text_color', 'text_color'
        ]

    def get_company_logo(self, obj):
        request = self.context.get('request')
        if obj.company_logo and request:
            return request.build_absolute_uri(obj.company_logo.url)
        elif obj.company_logo:
            return obj.company_logo.url
        return None

    def get_profile_picture(self, obj):
        request = self.context.get('request')
        if obj.profile_picture and request:
            return request.build_absolute_uri(obj.profile_picture.url)
        elif obj.profile_picture:
            return obj.profile_picture.url
        return None


        