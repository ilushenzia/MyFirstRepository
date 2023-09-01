from django.urls import path
from .views import index, top_sellers, adv_post, adv_view

urlpatterns = [
    path('', index, name = 'main'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('adv-post/', adv_post, name = 'adv-post'),
    path('advertisement/<int:pk>', adv_view, name='adv'),
]