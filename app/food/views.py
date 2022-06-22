from django.shortcuts import render

from django.http import HttpResponse
from .models import Food
from user.models import User


# showing the main page
def main(request):
    return render(request, 'food/main.html', {})


# numerator
def calculating(selected_features, foods):
    result_list = []
    numerator = 0
    for feature in selected_features.keys():
        print(selected_features[feature] == 'UD')
        if selected_features[feature] != 'UD':
            numerator += 1
    if numerator == 0:
        return 0
    for food in foods:
        denominator = 0
        # country
        if selected_features['country'] == food.country:
            denominator += 1
        # color
        if selected_features['color'] == food.color:
            denominator += 1
        # taste
        if selected_features['taste'] == food.taste:
            denominator += 1
        # protein
        if selected_features['protein'] == food.protein:
            denominator += 1
        # type
        if selected_features['type_food'] == food.type:
            denominator += 1
        # carbohydrate
        if selected_features['carbohydrate'] == food.carbohydrate:
            denominator += 1
        possibility = denominator / numerator
        print(possibility)
        if 0.4 <= possibility:
            result_list.append(food)
    return result_list


# Available Options
# taste
# country
# color
# protein
# type
# carbohydrate
def searching_foods(request):
    if request.method == 'POST':
        # a list of selected features to calculate
        feature_selected = {}
        country = request.POST['country']
        feature_selected['country'] = country
        taste = request.POST['taste']
        feature_selected['taste'] = taste
        color = request.POST['color']
        feature_selected['color'] = color
        protein = request.POST['protein']
        feature_selected['protein'] = protein
        type_food = request.POST['type']
        feature_selected['type_food'] = type_food
        carbohydrate = request.POST['carbohydrate']
        feature_selected['carbohydrate'] = carbohydrate

        print("FEATURE SELECTED")
        print(feature_selected)

        selected = Food.objects.filter(country=country,
                                       taste=taste,
                                       color=color,
                                       protein=protein,
                                       type=type_food,
                                       carbohydrate=carbohydrate)
        # If not perfect match
        if not selected:
            foods = calculating(selected_features=feature_selected, foods=Food.objects.all())
            if foods == 0:
                return render(request, 'food/main.html', {"warning": "You need to choose at least one feature"})
            context = {
                'foods': foods,
            }
            return render(request, 'food/main.html', context=context)
        else:
            context = {
                'foods': selected,
            }
            return render(request, 'food/main.html', context=context)


def food_detail(request, pk):
    food = Food.objects.get(pk=pk)
    context = {
        'food': food
    }
    return render(request, 'food/food_detail.html', context)


