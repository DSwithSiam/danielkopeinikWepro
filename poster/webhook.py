# views.py
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.models import CustomUser  # adjust to your app

stripe.api_key = settings.STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET = settings.STRIPE_WEBHOOK_SECRET  # from .env or settings.py




class StripeWebhookAPIView(APIView):
   
    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

        try:
            event = stripe.Webhook.construct_event(
                payload=payload, sig_header=sig_header, secret=STRIPE_WEBHOOK_SECRET
            )

        except ValueError as e:
            return Response({'error': 'Invalid payload'}, status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:
            return Response({'error': 'Invalid signature'}, status=status.HTTP_400_BAD_REQUEST)

        event_type = event["type"]
        data = event["data"]["object"]
        customer_id = data.get("customer")

        # Handle specific events
        if event_type == "checkout.session.completed":
            subscription_id = data.get("subscription")
            try:
                user = CustomUser.objects.get(stripe_customer_id=customer_id)
                print(f"Subscription completed for {user.email}")
                # You can update user profile or create Subscription object here
            except CustomUser.DoesNotExist:
                print("User not found")

        elif event_type == "invoice.paid":
            try:
                user = CustomUser.objects.get(stripe_customer_id=customer_id)
                print(f"Invoice paid by {user.email}")
            except CustomUser.DoesNotExist:
                pass

        elif event_type == "invoice.payment_failed":
            try:
                user = CustomUser.objects.get(stripe_customer_id=customer_id)
                print(f" Payment failed for {user.email}")
            except CustomUser.DoesNotExist:
                pass

        elif event_type == "customer.subscription.deleted":
            try:
                user = CustomUser.objects.get(stripe_customer_id=customer_id)
                print(f" Subscription canceled for {user.email}")
                # Optional: deactivate account or mark subscription inactive
            except CustomUser.DoesNotExist:
                pass

        # Add more event types as needed

        return Response({'status': 'success'}, status=status.HTTP_200_OK)
