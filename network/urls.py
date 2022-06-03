from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('unauthorized-access', views.unauthorized_access, name="authorization_problem"),
    path('profile-settings', views.profileEdit, name="edit"),
    path('additional-settings', views.additionalSettings, name="additionalSettings"),
    path('friendsPage', views.friendsPage, name="friendsPage"),
    path('createPost', views.createPost, name="createpost"),
    path('uploadPhoto', views.uploadPhoto, name="uploadPhoto"),
    path('createFilter', views.createFilter, name="createFilter")
]
