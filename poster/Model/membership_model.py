from django.db import models 


from code_snippet.membership_types import membership_types ,payment_status

from accounts.models import CustomUser 
from django.utils.timezone import now


class MemberShipPlan(models.Model):

   

    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    memebership_types = models.CharField(max_length=40, choices=membership_types,default='we_free',unique=True)
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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"memebership_types: {self.memebership_types} "
