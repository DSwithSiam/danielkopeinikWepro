from rest_framework import serializers
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'image', 'username', 'password', 'phone', 'bio']
        read_only_fields = ['id', 'username', 'bio']
        extra_kwargs = {
            'password': {'write_only': True},
            'image': {'required': False},
        }
        

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone=validated_data.get('phone', ''),
            email=validated_data['email'],
            username=validated_data['email'].split('@')[0],
            password=validated_data.get('password'),

        )
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.email = validated_data.get('email', instance.email)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


  
    



# Get User Serializer 


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'image', 'username', 'phone', 'bio']
      