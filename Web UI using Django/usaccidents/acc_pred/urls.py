from django.urls import path,include
from .import views 
from django.conf.urls.static import static

urlpatterns = [path('',views.home,name='SevirityPrediction.html'),
			   path('about.html',views.about,name='about')



]