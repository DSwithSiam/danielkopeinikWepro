from django.urls import path , include 
from poster.View.poster_view import PostModelViewSet 

from poster.View.membership_view import MembershipPlanViewSet
from poster.View.feature_view  import FetureBasePriceModelViewSet

from poster.webhook import StripeWebhookAPIView
from poster.View.checkout_session import CreateCheckOutSessionView

from rest_framework.routers import DefaultRouter


router = DefaultRouter()


router.register('registers',PostModelViewSet,basename='poster_urls')
router.register('membership',MembershipPlanViewSet,basename='membership_urls')
# router.register('user/membership',UserMembershipModelViewSet,basename='user_membership_urls')
router.register('feature/base/price',FetureBasePriceModelViewSet,basename='feature_urls')



urlpatterns = [
    path('', include(router.urls)),
    path('webhook/',StripeWebhookAPIView.as_view(),name='webhook'),
    path('create/checkout/',CreateCheckOutSessionView.as_view(),name='checkout'),

]
