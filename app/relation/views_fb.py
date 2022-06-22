from django.shortcuts import render

from food.models import Food
from user.models import User
from relation.models import Relation
import pyrebase

# creating relation instance between user and food with given food_pk and request.user
# request.user.pk to get user pk(primary key == id)
# pk in the parameter is to find food from food objects
def add_favorite_food(request, pk):
    if request.method == 'POST':
        user = request.user
        food = pk
        if Relation.objects.filter(user_like=user, food_liked=food) != None:
            food = Food.objects.get(pk=pk)
            context = {
                'food': food
            }
            return render(request, 'food/detail.html', context=context)
        relation = Relation.objects.create(user_like=user, food_liked=food)
        relation.save()
        # user = User.objects.get(pk=request.user.pk)
        # food = Food.objects.get(pk=pk)
        # relation = Relation.objects.create(user_like=user, food_liked=food)
        # relation.save()
    return render(request, 'food/main.html')


# removing relation instance between user and food with given food_pk and request.user
# request.user.pk to get user pk(primary key == id)
# pk in the parameter is to find food from food objects
def remove_favorite_food(request, pk):
    if request.method == 'POST':
        user = request.session['uid']
        food = pk
        relation = Relation.objects.filter(user_like=user, food_liked=food)
        relation.delete()
        print(relation)
        # # getting user object using request.user.pk -> returned type QuerySet
        # user = User.objects.get(pk=request.user.pk)
        # # getting food object using pk -> returned type QuerySet
        # food = Food.objects.get(pk=pk)
        # Relation.objects.delete(user_like=user, food_liked=food)
    return render(request, 'user/user_detail.html')


def user_list(request):
    user = request.session['uid']
    print(user)
    liked_relation = Relation.objects.filter(user_like=user)
    liked_food = []
    for i in liked_relation:
        food_liked = Food.objects.get(pk=i.food_liked)
        liked_food.append(food_liked)
    context = {
        'liked_food': liked_food,
    }
    return render(request, 'user/user_detail.html', context)
