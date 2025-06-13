from django.contrib import admin

# Register your models here.
from poster.Model.poster_model  import PosterModel 

from poster.Model.membership_model import MemberShipPlan 

from poster.Model.feature_model import FeatureBasePriceModel 



admin.site.register(PosterModel)
admin.site.register(MemberShipPlan)

admin.site.register(FeatureBasePriceModel)
