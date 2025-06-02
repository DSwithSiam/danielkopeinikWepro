from django.db import models 
from app_template.Model.app_template_model import AppTemplateModel 


class PosterModel(models.Model):

    app_template = models.ForeignKey(AppTemplateModel,related_name='app_posters',on_delete=models.CASCADE,null=True)
    description = models.TextField(null=True,blank=True)
    poster_image = models.ImageField(upload_to='app_template_images/', verbose_name='Upload poster image', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"apps poster : {self.app_template.title} , id : {self.id}"