from django.db import models
from django.conf import settings

from user.models import User


class Food(models.Model):
    english_name = models.CharField(max_length=100)
    original_name = models.CharField(max_length=100)
    UNDECIDED = 'UD'
    NOT_INCLUDED = 'NA'
    # country choices
    KOREA = 'KR'
    JAPAN = 'JP'
    COUNTRY_CHOICES = [
        (KOREA, 'Korean'),
        (JAPAN, 'Japanese'),
        (NOT_INCLUDED, 'Not Applied'),
        (UNDECIDED, 'Not sure')
    ]
    country = models.CharField(
        max_length=2,
        choices=COUNTRY_CHOICES,
        default=UNDECIDED,
    )
    # color choices
    YELLOW = 'YL'
    RED = 'RD'
    BROWN = 'BR'
    BLACK = 'BL'
    COLOR_CHOICES = [
        (YELLOW, 'Yellow'),
        (RED, 'Red'),
        (BROWN, 'Brown'),
        (BLACK, 'Black'),
        (NOT_INCLUDED, 'Not Applied'),
        (UNDECIDED, 'Not sure')
    ]
    color = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=UNDECIDED,
    )
    # taste choices
    SWEET = 'SW'
    SPICY = 'SC'
    SOUR = 'SR'
    SALTY = 'SL'
    BITTER = 'BT'
    TASTE_CHOICES = [
        (SWEET, 'Sweet'),
        (SPICY, 'Spicy'),
        (SOUR, 'Sour'),
        (SALTY, 'Salty'),
        (BITTER, 'Bitter'),
        (NOT_INCLUDED, 'Not Applied'),
        (UNDECIDED, 'Not sure'),
    ]
    taste = models.CharField(
        max_length=2,
        choices=TASTE_CHOICES,
        default=UNDECIDED,
    )
    # protein choices
    BEEF = 'BF'
    PORK = 'PR'
    FISH = 'FS'
    SHELLFISH = 'SF'
    CHICKEN = 'CK'
    VEGETARIAN = 'VG'
    PROTEIN_CHOICES = [
        (BEEF, 'Beef'),
        (PORK, 'Pork'),
        (SHELLFISH, 'Shell fish'),
        (FISH, 'Fish'),
        (VEGETARIAN, 'Vegetarian'),
        (CHICKEN, 'Chicken'),
        (NOT_INCLUDED, 'No Meat'),
        (UNDECIDED, 'Not sure'),
    ]
    protein = models.CharField(
        max_length=2,
        choices=PROTEIN_CHOICES,
        default=UNDECIDED,
    )
    # type choices (how the food being prepared)
    BOILED = 'BD'
    FRIED = 'FR'
    STEAMED = 'ST'
    BAKED = 'BE'
    BARBEQUE = 'BQ'
    RAW = 'RW'
    TYPE_CHOICES = [
        (BOILED, 'Boiled'),
        (FRIED, 'Fried'),
        (STEAMED, 'Steamed'),
        (BAKED, 'Baked'),
        (BARBEQUE, 'Barbeque'),
        (RAW, 'Raw'),
        (NOT_INCLUDED, 'Not Applied'),
        (UNDECIDED, 'Not sure'),
    ]
    type = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default=UNDECIDED,
    )
    # Carbohydrates
    NOODLES = 'ND'
    RICE = 'RE'
    CAR_CHOICES = [
        (NOODLES, "Noodles"),
        (RICE, "Rice"),
        (NOT_INCLUDED, 'Not Applied'),
        (UNDECIDED, "Not sure"),
    ]
    carbohydrate = models.CharField(
        max_length=2,
        choices=CAR_CHOICES,
        default=UNDECIDED,
    )
    food_description = models.TextField(max_length=1000, blank=True)
    food_link = models.URLField(max_length=200, blank=True)
    food_image = models.ImageField(upload_to='food', blank=True)

    # list of descriptions for phase 2
    # descriptions = []

    def __str__(self):
        return self.original_name
