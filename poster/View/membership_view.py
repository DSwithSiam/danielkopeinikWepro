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

    # def get_permissions(self):
    #     if self.action in ('create', 'update', 'partial_update', 'destroy'):
    #         return [IsAdminUser()]
    #     return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action in ('create','update','partial_update','destroy'):
            return MembershipPlanSerializer
        return GetMembershipPlanSerializer

    @action(detail=True, methods=['post'], url_path='create-checkout-session')
    def create_checkout_session(self, request, pk=None):
        plan = self.get_object()
        user = request.user

        if plan.amount == 0:
            return Response({"detail": "Free plan does not require payment."}, status=status.HTTP_400_BAD_REQUEST)

        if not plan.stripe_price_id:
            return Response({"detail": "Stripe price ID missing. Please contact admin."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Ensure Stripe customer exists
        if not user.stripe_customer_id:
            customer = stripe.Customer.create(email=user.email)
            user.stripe_customer_id = customer.id
            user.save()
        else:
            customer = user.stripe_customer_id

        # Create Checkout Session
        session = stripe.checkout.Session.create(
            customer=customer,
            payment_method_types=["card"],
            line_items=[{
                "price": plan.stripe_price_id,
                "quantity": 1,
            }],
            mode="subscription",
            success_url='https://gameplanai.co.uk',  # Change to your success URL
            cancel_url='https://gameplanai.co.uk', # Change to your cancel URL
        )

        # Save session ID in the plan
        plan.stripe_checkout_session_id = session.id
        plan.save(update_fields=['stripe_checkout_session_id'])

        return Response({'checkout_url': session.url})

