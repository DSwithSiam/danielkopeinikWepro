import stripe 
from django.conf import settings 
from stripe.error import StripeError


stripe.api_key = settings.STRIPE_SECRET_KEY


def has_active_subscription(email):

    try:

        customers = stripe.Customer.list(email=email)

        if not customers.data:
            
            return False, "No customer found with this email"
        
        for customer in customers.data:
            subscriptions = stripe.Subscription.list(customer=customer.id, status='active')
            if subscriptions.data:
                return True, "Active subscription found"
            
        return False, "No active subscription found"
    
    except StripeError as e:
        return False, f"Stripe error: {str(e)}"

