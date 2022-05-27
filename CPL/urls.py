from django.urls import path

from CPL import views

urlpatterns = [
    path('register_for_logged_user', views.register_user_for_a_ride, name='register_for_logged_user'),
    path('login_user_from_modal', views.login_user_from_modal, name='login_user_from_modal'),
    path('', views.show_cycling_events, name='home'),
    path('show_user_cookies', views.show_user_cookies, name='show_user_cookies')
]
