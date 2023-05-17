from django.urls import path
from .views import dashboard, profile_list, profile, uploadPage

app_name = "petstagram"
urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("upload/",uploadPage, name="uploadPage"),
]