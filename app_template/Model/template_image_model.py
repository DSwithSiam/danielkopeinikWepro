from django.db import models 

from app_template.Model.app_template_model import AppTemplateModel 



class TemplateImageModel(models.Model):


    image = models.ImageField(upload_to='app_template_images/', verbose_name='Upload Image', null=True, blank=True)
    image_title = models.CharField(max_length=250,null=True,blank=True)
    template= models.ForeignKey(AppTemplateModel,related_name='template_images',on_delete=models.CASCADE,null=True)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At') 


    def __str__(self):
        return f"image title : {self.image_title}"
