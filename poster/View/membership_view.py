from rest_framework.viewsets import ModelViewSet 

from rest_framework.permissions import IsAuthenticated,IsAdminUser


from poster.Model.membership_model import MemberShipPlan 

from poster.Serializer.membership_serializer import MembershipPlanSerializer



class MembershipPlanViewSet(ModelViewSet):

    queryset = MemberShipPlan.objects.all()
    serializer_class = MembershipPlanSerializer
    # permission_class = [IsAuthenticated]


    def get_permission(self):

        if self.action in ('create','update','partial_update','destroy'):
            permission_classes = [IsAdminUser]

        else:
            permission_classes = [IsAuthenticated]

        return [ permission() for permission in permission_classes ]

