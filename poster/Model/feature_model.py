from django.db import models 


class FeatureBasePriceModel(models.Model):

    # this all value used for single feature price setup
    posting_generation = models.FloatField(default=0.0)
    custom_app = models.FloatField(default=0.0)
    ai_inclusion = models.FloatField(default=0.0)
    custom_design_inclusion = models.FloatField(default=0.0)
    color_design_inclusion = models.FloatField(default=0.0)
    logo_design_inclusion = models.FloatField(default=0.0)
    we_pro_branding = models.FloatField(default=0.0)


    def __str__(self) -> str:
        return f"feature id : {self.pk}"

    


