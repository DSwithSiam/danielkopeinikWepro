from rest_framework import serializers 
from  poster.Model.user_membership_model import UserMemberShipPlan 

from poster.Serializer.membership_serializer import MembershipPlanSerializer 

from accounts.serializers import GetUserSerializer 





class CreateUserMemberShipSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserMemberShipPlan
        fields = '__all__'



class GetUserMemberShipSerializer(serializers.ModelSerializer):

    user=GetUserSerializer(read_only=True,many=False)
    membership_plan= MembershipPlanSerializer(read_only = True, many=False)


    class Meta:

        model = UserMemberShipPlan
        fields = '__all__'