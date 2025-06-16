from  django.db import models 



class BrandModel(models.Model):

    company_name = models.CharField(max_length=200, unique=True)
    company_logo = models.ImageField(upload_to='app_template_images/', verbose_name='company logo image', null=True, blank=True)
    facebook_link = models.TextField(null=True,blank=True)
    instagram_link = models.TextField(null=True,blank=True)
    twiter_link = models.TextField(null=True,blank=True)
    linkedin_link = models.TextField(null=True,blank=True)
    hotel_website_link = models.TextField(null=True,blank=True)
    profile_name = models.CharField(max_length=200,null=True,blank=True)
    hotel_location = models.TextField(null=True,blank=True)
    main_color = models.CharField(max_length=200,null=True,blank=True)
    background_color = models.CharField(max_length=200,null=True,blank=True)
    heading_text_color = models.CharField(max_length=200,null=True,blank=True)
    text_color = models.CharField(max_length=200,null=True,blank=True)



    def __str__(self) -> str:
        return f"company name : {self.company_name}"
    



