from django.db import models 

from accounts.models import CustomUser
from code_snippet.subscription_category import subscription_category  

from django.contrib.postgres.fields import JSONField
import uuid
from django.core.files.base import ContentFile
from io import BytesIO
import qrcode


class AppTemplateModel(models.Model):

    app_category = models.CharField(
        max_length=50,
        choices=subscription_category,
        default='prices_lists',
        verbose_name='prices Lists'
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True,null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='app_templates')
    title = models.CharField(max_length=255, verbose_name='Title',db_index=True)
    email = models.EmailField(max_length=255, verbose_name='Email', null=True, blank=True)
    contact = models.CharField(max_length=20, verbose_name='Contact', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True) 
    upload_banner = models.ImageField(upload_to='app_template_images/', verbose_name='Upload Banner', null=True, blank=True)
    checkin_time = models.TimeField(verbose_name='Check-in Time', null=True, blank=True)
    checkout_time = models.TimeField(verbose_name='Check-out Time', null=True, blank=True)
    trips_adventure_category = models.CharField(max_length=50, verbose_name='Trips and Adventure Category',null=True,  blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)



   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At') 


    def __str__(self):
        return f"{self.title} - {self.app_category}" 
    

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new and not self.qr_code:
            # Use the UUID to generate QR code content
            qr_data = f"{self.uuid}/"  # or just str(self.uuid)
            qr = qrcode.make(qr_data)
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            filename = f'qr_code_{self.pk}.png'

            self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)
            super().save(update_fields=['qr_code'])


