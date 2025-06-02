from django.contrib import admin

# Register your models here.
from poster.Model.poster_model  import PosterModel 

from poster.Model.membership_model import MemberShipPlan 

admin.site.register(PosterModel)

admin.site.register(MemberShipPlan)