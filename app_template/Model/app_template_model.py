from django.db import models 

from accounts.models import CustomUser
from code_snippet.subscription_category import subscription_category  


class AppTemplateModel(models.Model):

    app_category = models.CharField(
        max_length=50,
        choices=subscription_category,
        default='prices_lists',
        verbose_name='rices Lists'
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='app_templates')
    title = models.CharField(max_length=255, verbose_name='Title',unique=True,db_index=True)
    email = models.EmailField(max_length=255, verbose_name='Email', null=True, blank=True)
    contact = models.CharField(max_length=20, verbose_name='Contact', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True) 
    upload_banner = models.ImageField(upload_to='app_template_images/', verbose_name='Upload Image', null=True, blank=True)
    checkin_time = models.TimeField(verbose_name='Check-in Time', null=True, blank=True)
    checkout_time = models.TimeField(verbose_name='Check-out Time', null=True, blank=True)
    trips_adventure_category = models.CharField(max_length=50, verbose_name='Trips and Adventure Category', null=True, blank=True)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At') 






  
    def __str__(self):
        return self.name