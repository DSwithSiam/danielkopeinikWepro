
from django.conf import settings 
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from django.urls import reverse  
import stripe 
import logging

stripe.api_key = settings.STRIPE_SECRET_KEY




class CreateCheckOutSessionView(APIView):


    def post(self,request):

        product_name = request.data.get('product_name','').strip()
        custom_amount = request.data.get('custom_amount','').strip()

        
        try:
            if product_name:

                if not hasattr(settings, 'STRIPE_PRODUCT_PRICES'):
                        return Response({'error': 'Product prices not configured'},status=status.HTTP_400_BAD_REQUEST)
                
                price_id = settings.STRIPE_PRODUCT_PRICES.get(product_name)

                if not price_id:

                    
                    return Response({'error':'Invalid Product,please try again'},status=status.HTTP_400_BAD_REQUEST)
                


                  # Optional validation to ensure price_id exists in Stripe
                try:
                    stripe.Price.retrieve(price_id)
                except stripe.error.InvalidRequestError:
                    return Response({'error': f"Stripe price ID '{price_id}' not found or not accessible."}, status=status.HTTP_400_BAD_REQUEST)

                line_items = [
                    {
                        'price':price_id,
                        'quantity':1

                    }
                ]
                
            elif custom_amount:
                
                try:
                    custom_amount = float(custom_amount)

                    if custom_amount<0:
                        raise ValueError

                except ValueError:
                    return Response({'error': 'Invalid custom amount'}, status=status.HTTP_400_BAD_REQUEST)
                

                line_items = [{
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Custom Subscription',
                            },
                            'unit_amount': int(custom_amount * 100),
                            'recurring': {
                                'interval': 'month',
                            },
                        },
                        'quantity': 1,
                    }]
                
            else :
                
                return Response({'error':'Invalid Product Id'},status=status.HTTP_400_BAD_REQUEST)
            
            
            checkout_session = stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='subscription',
                    # success_url=request.build_absolute_uri(reverse('success')),
                    # cancel_url=request.build_absolute_uri(reverse('cancel')),
                    success_url='https://gameplanai.co.uk',  # Change to your success URL
                    cancel_url='https://gameplanai.co.uk', # Change to your cancel URL
                    # metadata={'user_id': str(user.pk), "package": subscription_plan},
                )
            return Response({'sessionurl': checkout_session.url}, status=status.HTTP_200_OK)
        

        except stripe.error.StripeError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)