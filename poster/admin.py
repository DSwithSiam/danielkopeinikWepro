from django.contrib import admin

# Register your models here.
from poster.Model.poster_model  import PosterModel 

from poster.Model.membership_model import MemberShipPlan 
from poster.Model.user_membership_model import UserMemberShipPlan
<<<<<<< HEAD
=======
from poster.Model.feature_model import FeatureBasePriceModel 

>>>>>>> feature_test


admin.site.register(PosterModel)
admin.site.register(MemberShipPlan)
<<<<<<< HEAD
admin.site.register(UserMemberShipPlan)
=======
admin.site.register(UserMemberShipPlan)
admin.site.register(FeatureBasePriceModel)
>>>>>>> feature_test
