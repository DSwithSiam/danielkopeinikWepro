from rest_framework.viewsets import ModelViewSet 


from poster.Serializer.user_membership_serializer import (
    CreateUserMemberShipSerializer,
    GetUserMemberShipSerializer
)


from poster.Model.user_membership_model import UserMemberShipPlan 



class UserMembershipModelViewSet(ModelViewSet):

    queryset = UserMemberShipPlan.objects.select_related(
        'membership_plan',
        'user'
    )

    def get_serializer_class(self):

        if self.action in ['create','update','partial-update','destroy']:
            return CreateUserMemberShipSerializer
        
        return GetUserMemberShipSerializer