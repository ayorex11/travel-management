from django.urls import path 
from . import views

urlpatterns=[
	path('CalculateAmount/',views.CalculateAmount),
	path('makepayment/',views.makepayment),
	path('bill/',views.bill),

]