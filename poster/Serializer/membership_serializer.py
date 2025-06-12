from rest_framework import serializers 

from poster.Model.membership_model import MemberShipPlan

class MembershipPlanSerializer(serializers.ModelSerializer):

    class Meta:

        model = MemberShipPlan
        fields = '__all__'
