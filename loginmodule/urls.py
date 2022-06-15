from django.urls import path
from . import views 

urlpatterns= [
	path('home/',views.home),
    path('login/',views.login),
    path('logout/',views.logout),
    path('auth/',views.auth_view),
    path('aboutus/',views.aboutus),

]