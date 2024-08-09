from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'registerpage'),
    path('profile/', views.profile, name = 'profilepage'),
    path('profile/changeuserdata/', views.change_user_data, name = 'changedatapage'),
    path('profile/changeuserdata/pass_change/', views.pass_change, name = 'passchangepage'),
    path('profile/changeuserdata/pass_change2/', views.pass_change2, name = 'passchangepage2'),
    path('login/', views.user_login, name = 'loginpage'),
    path('logout/', views.user_logout, name = 'logoutpage'),

]