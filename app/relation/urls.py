from django.urls import path

from .views import *

app_name = 'relation'
urlpatterns = [
    # to create food favorite
    path('add/<int:pk>/', add_favorite_food, name='add-favorite-food'),
    # to delete food favorite
    path('remove/<int:pk>/', remove_favorite_food, name='remove-favorite-food'),
    path('userlikes/', user_favorites, name='user-list'),
]
