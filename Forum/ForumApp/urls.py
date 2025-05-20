from django.urls import path
from ForumApp.views import *

urlpatterns = [
    path('', home, name='homePage'),
    path('home/', home, name='homePage'),
    path('newcategory/', createCard, name='add_category'),
    path('remove/delete/<int:pk>', removeCategory, name='removeCategory'),
    path('registration/', register_user_view, name='newUser'),
    path('login/', authorizeUser, name='loginPage'),
    path('category/<int:pk>/', category_detail, name='categoryPage'),
    path('card/<int:card_id>/', card_detail, name='card_detail'),
    path('addcategory/', createCategory, name='newPost'), 
    path('category/<int:pk>/add-post/', add_post, name='add_post'),
    
    path('post/<int:pk>/', post_detail, name='post_detail'),
]


