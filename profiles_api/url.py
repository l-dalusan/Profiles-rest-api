from django.urls import patch

from profiles_api import views


urlpatterns = [
path('hello=view/', views.HelloApiView.as_view()),
]
