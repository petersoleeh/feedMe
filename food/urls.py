from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #the landing page
    url(r'^$',views.index,name='index'),

    #the restaurants page
    url(r'^food/(?P<food_id>[0-9]+)/$',views.restaurant,name='rest'),

    #the restaurant-details page
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$',views.restaurant_details,name='rest-details')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
