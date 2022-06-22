from django.shortcuts import render, redirect

from food.models import Food
from user.models import User
from relation.models import Relation


def add_favorite_food(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        food = Food.objects.get(pk=pk)
        context = {
            'food': food,
        }
        # duplicate prevention
        if Relation.objects.filter(user_like=user, food_liked=food):
            context = {
                'food': food,
                'message': 'You already added into your favorites'
            }
            return render(request, 'food/food_detail.html', context=context)
        relation = Relation.objects.create(user_like=user, food_liked=food)
        relation.save()
        return render(request, 'food/food_detail.html', context=context)


def remove_favorite_food(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        food = Food.objects.get(pk=pk)
        relation = Relation.objects.get(user_like=user, food_liked=food)
        relation.delete()
        user_liked = Relation.objects.filter(user_like=user)
        context = {
            'liked_foods': user_liked,
        }
        return redirect('relation:user-list')


def user_favorites(request):
    user = User.objects.get(pk=request.user.pk)
    print(user)
    user_likes = Relation.objects.filter(user_like=user)
    print(user_likes)
    liked_foods = []
    for user_like in user_likes:
        liked_foods.append(user_like.food_liked)
    context = {
        'liked_foods': liked_foods,
    }
    return render(request, 'user/user_detail.html', context=context)
