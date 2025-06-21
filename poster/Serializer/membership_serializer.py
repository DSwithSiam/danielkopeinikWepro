from rest_framework import serializers 

from poster.Model.membership_model import MemberShipPlan

from accounts.serializers  import GetUserSerializer 



class MembershipPlanSerializer(serializers.ModelSerializer):

    class Meta:

        model = MemberShipPlan
        fields = '__all__'


class GetMembershipPlanSerializer(serializers.ModelSerializer):


    customer= GetUserSerializer(read_only=True,many=False)
    class Meta:

        model = MemberShipPlan
        fields = '__all__'
