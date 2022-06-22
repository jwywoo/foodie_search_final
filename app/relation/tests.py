from django.test import TestCase
from food.models import *
from user.models import *
from .models import Relation

class TestViews(TestCase):

     # Setup database
    def setUp(self):
        Food.objects.create(english_name='Rice', original_name='Rice', country='JP')
        Food.objects.create(english_name='Ramen', original_name='Ramen', country='JP', color='YL', taste='SL', protein='PR', type='BD', carbohydrate='ND')
        Food.objects.create(english_name='Spicy Ramen', original_name='Spicy Ramen', country='JP', color='RD', taste='SL', protein='PR', type='BD', carbohydrate='ND')

    #######################################################
    # ~~~~~~~~~~~~ TESTS FOR USER_FAVORITES ~~~~~~~~~~~~~ #
    #######################################################   

    def test_user_favorites_Empty(self):

        # Create user and login
        User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        self.client.login(username='paul',password='password')

        response = self.client.get('/relation/userlikes/')

        # Liked foods should be 0
        self.assertEquals(len(response.context['liked_foods']), 0)


    def test_user_favorites_NotEmpty(self):

        # Create user and login
        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        self.client.login(username='paul',password='password')

        # Create food
        food = Food.objects.get(pk=1)

        # Add food as a liked food manually
        Relation.objects.create(user_like=user, food_liked=food)

        # check if food is indeed in userlikes 
        response = self.client.get('/relation/userlikes/')
        self.assertEquals(response.context['liked_foods'][0], food)

    # INTEGRATION TESTING add_favorite -> check favorites
    ######################################################
    # ~~~~~~~~~~ TESTS FOR ADD_FAVORITE_FOOD ~~~~~~~~~~~ #
    #######################################################  

    def test_add_favorite_food(self):
        
        # Create user and login
        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        self.client.login(username='paul',password='password')

        # add Rice as favorite food
        response = self.client.post('/relation/add/1/')

        # check if Rice is indeed in userlikes 
        food = Food.objects.get(pk=1)
        response = self.client.get('/relation/userlikes/')
        self.assertEquals(response.context['liked_foods'][0], food)

    
    def test_add_favorite_food_duplicate(self):

        # Create user and login
        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        self.client.login(username='paul',password='password')

        # add Rice as favorite food
        response = self.client.post('/relation/add/1/')

        # check if Rice is indeed in userlikes 
        food = Food.objects.get(pk=1)
        response = self.client.get('/relation/userlikes/')
        self.assertEquals(response.context['liked_foods'][0], food)

        # add Rice as favorite food AGAIN
        response = self.client.post('/relation/add/1/')
        self.assertEquals(response.context['message'], 'You already added into your favorites')

        # Go to userlikes
        response = self.client.get('/relation/userlikes/')

        # Check that rice is still there and no duplicate occurs
        self.assertEquals(response.context['liked_foods'][0], food)
        self.assertEquals(len(response.context['liked_foods']), 1)


    def test_add_favorite_food_GetRequest(self):

        # This does nothing for the meanwhile other than 
        # cover branch
        try:
            response = self.client.get('/relation/add/1/')
            self.fail("It should expect a get not post")

        except ValueError:
            pass

    # INTEGRATION TESTING add_favorite -> check favorites -> remove_favorite -> check favorites
    ######################################################
    # ~~~~~~~~ TESTS FOR REMOVE_FAVORITE_FOOD ~~~~~~~~~~ #
    ####################################################### 

    def test_remove_favorite_food(self):

        # Create user and login
        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        self.client.login(username='paul',password='password')

        # add Rice as favorite food
        response = self.client.post('/relation/add/1/')

        # check if Rice is indeed in userlikes 
        food = Food.objects.get(pk=1)
        response = self.client.get('/relation/userlikes/')
        self.assertEquals(response.context['liked_foods'][0], food)

        # Remove Rice from userlikes
        response = self.client.post('/relation/remove/1/')
        response = self.client.get('/relation/userlikes/')

        # Nothing should be in userlikes anymore
        self.assertEquals(len(response.context['liked_foods']), 0)


    def test_remove_favorite_food_GetRequest(self):
        
        # This does nothing for the meanwhile other than 
        # cover branch
        try:
            response = self.client.get('/relation/remove/1/')
            self.fail("It should expect a get not post")

        except ValueError:
            pass


