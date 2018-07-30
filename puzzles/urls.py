from django.urls import path
from . import views

app_name="users"
urlpatterns = [
    path("submit",views.submit,name="submit"),
    path("grade",views.grade,name="grade"),
    path("scoreboard",views.scoreboard,name="scoreboard"),
    ]
