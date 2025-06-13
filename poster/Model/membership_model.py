from django.db import models 


from code_snippet.membership_types import membership_types 


class MemberShipPlan(models.Model):

    memebership_types = models.CharField(max_length=40, choices=membership_types,default='we_free',unique=True)
    posting_generation= models.IntegerField(default=0)
    custom_app = models.IntegerField(default=0)
    is_ai_included = models.BooleanField(default=False)
    ai_chatbot_message_quantity=models.IntegerField(default=0)
    is_custom_design_included = models.BooleanField(default=False)
    is_color_section_included = models.BooleanField(default=False)
    is_only_logo = models.BooleanField(default=False)
    is_wepro_branding= models.BooleanField(default=False)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f" memebership_types: {self.memebership_types} "
