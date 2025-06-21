from django.db import models 
from accounts.models import CustomUser 
from app_template.Model.app_template_model import AppTemplateModel 



class AppVisitModel(models.Model):


    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='user_visits_app')
    template =models.ForeignKey(AppTemplateModel,related_name='visited_template',on_delete=models.CASCADE)

    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)