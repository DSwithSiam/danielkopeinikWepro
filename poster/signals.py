from django.db.models.signals  import pre_save ,post_save

from django.dispatch import receiver 

from poster.Model.membership_model  import MemberShipPlan 



@receiver(pre_save, sender=MemberShipPlan)

def set_membership_defaults(sender, instance, **kwargs):
    if instance.memebership_types == 'we_free':
        instance.amount = 0
        instance.custom_app = 1
        instance.posting_generation = 2
        instance.is_ai_included = False
        
        instance.ai_chatbot_message_quantity=0 
        instance.is_custom_design_included =False 
        instance.is_color_section_included =False
        instance.is_only_logo = True 
        instance.is_wepro_branding= True 

    elif instance.memebership_types == 'we_basic':
        instance.amount = 2499
        instance.custom_app = 2
        instance.posting_generation = 10
        instance.is_ai_included = False
        
        instance.ai_chatbot_message_quantity=200
        instance.is_custom_design_included =True 
        instance.is_color_section_included =True 
        instance.is_only_logo = True 
        instance.is_wepro_branding= True 
        
    elif instance.memebership_types == 'we_pro':
        
        instance.amount = 4499
        instance.custom_app = 4
        instance.posting_generation = 35
        instance.is_ai_included = True 
        
        instance.ai_chatbot_message_quantity=1500
        instance.is_custom_design_included =True 
        instance.is_color_section_included =True 
        instance.is_only_logo = True 
        instance.is_wepro_branding= False 