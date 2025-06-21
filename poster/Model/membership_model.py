from django.db import models 
import stripe 

from code_snippet.membership_types import membership_types ,payment_status
from accounts.models import CustomUser 
from django.utils.timezone import now


from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class MemberShipPlan(models.Model):

   

    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    memebership_types = models.CharField(max_length=40, choices=membership_types,default='we_free')
    posting_generation= models.IntegerField(default=0)
    custom_app = models.IntegerField(default=0)
    is_ai_included = models.BooleanField(default=False)
    ai_chatbot_message_quantity=models.IntegerField(default=0)
    is_custom_design_included = models.BooleanField(default=False)
    is_color_section_included = models.BooleanField(default=False)
    is_only_logo = models.BooleanField(default=False)
    is_wepro_branding= models.BooleanField(default=False)




    status = models.CharField(max_length=50,choices=payment_status,default='processing')
    stripe_payment_intent_id = models.CharField(max_length=255, null=True)
    amount = models.PositiveIntegerField(help_text="Amount in cents",default=0)
    currency = models.CharField(max_length=10, default='usd')

    stripe_product_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_price_id = models.CharField(max_length=255, null=True, blank=True)
    stripe_checkout_session_id = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"memebership_types: {self.memebership_types}"
    
    def save(self, *args, **kwargs):
        creating = not self.pk
        super().save(*args, **kwargs)

        if creating and self.amount > 0 and (not self.stripe_product_id or not self.stripe_price_id):
            # 1. Create Product in Stripe
            product = stripe.Product.create(name=f"{self.memebership_types} plan for {self.customer.email}")

            # 2. Create Price in Stripe
            price = stripe.Price.create(
                unit_amount=self.amount,
                currency=self.currency,
                product=product.id,
                recurring={"interval": "month"}  # Assuming monthly
            )

            # 3. Store Stripe info
            self.stripe_product_id = product.id
            self.stripe_price_id = price.id

            # 4. Save again
            super().save(update_fields=['stripe_product_id', 'stripe_price_id'])
