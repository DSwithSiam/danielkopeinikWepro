from django.db import models 

from poster.Model.membership_model import MemberShipPlan

from accounts.models import CustomUser 



class UserMemberShipPlan(models.Model):

    payment_status = (
        ('requires_payment_method', 'Requires Payment Method'),
        ('requires_confirmation', 'Requires Confirmation'),
        ('requires_action', 'Requires Action'),
        ('processing', 'Processing'),
        ('succeeded', 'Succeeded'),
        ('canceled', 'Canceled'),
    )

    user = models.OneToOneField(CustomUser,related_name='user_membership',on_delete=models.CASCADE)
    membership_plan = models.ForeignKey(MemberShipPlan,related_name='subscription_plans',on_delete=models.CASCADE)
    stripe_payment_intent_id = models.CharField(max_length=255, unique=True)
    amount = models.PositiveIntegerField(help_text="Amount in cents")
    currency = models.CharField(max_length=10, default='usd')
    status = models.CharField(max_length=50,choices=payment_status,default='processing')  # e.g. 'requires_payment_method', 'succeeded'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment {self.stripe_payment_intent_id} - {self.status}"