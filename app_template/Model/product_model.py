from django.db import models 
from app_template.Model.app_template_model import AppTemplateModel 


class ProductModel(models.Model):

    template = models.ForeignKey(AppTemplateModel,related_name='product_template',on_delete=models.CASCADE,null=True)
    product_name = models.CharField(max_length=250,db_index=True,unique=True)
    price = models.FloatField(default=0.0)
    product_image =models.ImageField(upload_to='app_template_images/', verbose_name='Product Image', null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"product name : {self.product_name}"
    
    class Meta:
        ordering = ['id']  # or another appropriate field