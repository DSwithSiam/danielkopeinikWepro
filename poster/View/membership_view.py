from rest_framework.viewsets import ModelViewSet 

from rest_framework.permissions import IsAuthenticated

from poster.Model.membership_model import MemberShipPlan 

from poster.Serializer.membership_serializer import MembershipPlanSerializer



class MembershipPlanViewSet(ModelViewSet):

    queryset = MemberShipPlan.objects.all()
    serializer_class = MembershipPlanSerializer
    # permission_class = [IsAuthenticated]