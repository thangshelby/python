from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logout",views.sayBye,name='sayBye'),
    # path('hello',views.scraping,name='hello'),
    path('form',views.form,name='form'),
    # path('scrap',views.scraping,name='scrap')    
]
