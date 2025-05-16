from django.urls import path
from ForumApp.views import home

urlpatterns = [
    path('test/', home, name='homePage')
]


