from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main"),
    path('unauthorized-access', views.unauthorized_access, name="authorization_problem")
]
