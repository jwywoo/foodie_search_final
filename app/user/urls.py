from django.urls import path

from .views import *

app_name = 'user'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signUp/', user_signup, name="user-create"),
    # path('postsignUp/', postsign_up),
]
