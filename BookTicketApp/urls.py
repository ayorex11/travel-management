from django.urls import path 
from . import views 

urlpatterns = [
	path('',views.bookticket),
	path('bookingdataadd/',views.bookingdataadd),
	path('booking_history/', views.booking_history),
	path('delete/',views.delete),
	path('feedback/',views.feedback),

]