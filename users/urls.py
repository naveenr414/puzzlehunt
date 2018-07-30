from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('login/submit',views.submit,name='submit'),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('create',views.create,name='create'),
    ]
