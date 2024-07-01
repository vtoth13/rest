from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.table_list, name='table_list'),
    path('menu/', views.menu_list, name='menu_list'),
    path('booking/create/', views.booking_create, name='booking_create'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('check-table-availability/<int:table_id>/<int:number_of_people>/', views.check_table_availability, name='check_table_availability'),
]