from rest_framework.viewsets import ModelViewSet 

from rest_framework.permissions import IsAuthenticated,IsAdminUser


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

from poster.Model.membership_model import MemberShipPlan 

from poster.Serializer.membership_serializer import (
    
    MembershipPlanSerializer,
    GetMembershipPlanSerializer

)



class MembershipPlanViewSet(ModelViewSet):

    queryset = MemberShipPlan.objects.select_related('customer')
    permission_classes = [IsAuthenticated]


    def get_serializer_class(self):
        if self.action in ('create','update','partial_update','destroy'):
            return MembershipPlanSerializer
        return GetMembershipPlanSerializer
     
    def perform_create(self,serializer):
        serializer.save(customer=self.request.user)





        