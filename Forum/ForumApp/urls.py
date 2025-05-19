from django.urls import path
from ForumApp.views import *

urlpatterns = [
    path('home/', home, name='homePage'),
    path('newcategory/', createCard, name='add_category'),
    path('remove/delete/<int:pk>', removeCategory, name='removeCategory'),
    path('registration/', register_user_view, name='newUser'),
    path('login/', authorizeUser, name='loginPage'),
    path('category/<int:pk>/', category_detail, name='categoryDetail'),
    
]


