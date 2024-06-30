from django.urls import path
from. import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('customer-login/', views.customer_login_view, name='customer_login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]