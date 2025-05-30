from django.contrib import admin

# Register your models here.
from app_template.Model.app_template_model import AppTemplateModel 

from app_template.Model.template_image_model import TemplateImageModel

from app_template.Model.product_model  import ProductModel



admin.site.register(AppTemplateModel) 
admin.site.register(TemplateImageModel)


admin.site.register(ProductModel)

