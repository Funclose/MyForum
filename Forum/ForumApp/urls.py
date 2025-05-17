from django.urls import path
from ForumApp.views import *

urlpatterns = [
    path('home/', home, name='homePage'),
    path('newcategory/', createCategory, name='add_category'),
    path('remove/delete/<int:pk>', removeCategory, name='removeCategory')
]


