from django.test import TestCase
from food.models import *
from .models import User
from .views import *

class TestViews(TestCase):

    # Setup database
    def setUp(self):
        Food.objects.create(english_name='Rice', original_name='Rice', country='JP')
        Food.objects.create(english_name='Ramen', original_name='Ramen', country='JP', color='YL', taste='SL', protein='PR', type='BD', carbohydrate='ND')
        Food.objects.create(english_name='Spicy Ramen', original_name='Spicy Ramen', country='JP', color='RD', taste='SL', protein='PR', type='BD', carbohydrate='ND')

    #####################################################
    #~~~~~~~~~~~~~ TESTS FOR USER_SIGNUP ~~~~~~~~~~~~~~ #
    #####################################################

    def test_user_signup_Valid(self):

        # Mock input for signup
        data = {
            'username': 'paul',
            'email' : 'paulabijaber@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post('/user/signUp/', data=data)

        # Check if site exists and Databse contains my info
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.get(pk=1).username, 'paul')
        

    def test_user_signup_NotValid(self):

        # Mock input for signup
        data = {
            'username': 'paul',
            'email' : 'paulabijaber@gmail.com',
            'password': 'password',
            'password2': 'passwdwasdord'
        }
        response = self.client.post('/user/signUp/', data=data)

        # Check if site exists and signup failed so database doesnt contain anything
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(User.objects.all()), 0)


    def test_user_signup_GetRequest(self):

        response = self.client.get('/user/signUp/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Signup Here!")

    #####################################################
    #~~~~~~~~~~~~~ TESTS FOR USER_LOGIN  ~~~~~~~~~~~~~~ #
    #####################################################

    def test_user_login_Valid(self):

        # Create User instance in database
        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        response = self.client.login(username='paul',password='password')

        # Check if user is logged in and it exists
        self.assertTrue(response)
        self.assertEqual(User.objects.get(pk=1), user)


    def test_user_login_NotValid(self):

        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        response = self.client.login(username='paul',password='pawdas')

        # Check that login failed
        self.assertFalse(response)

        # Check that failed login prints correct message
        response = self.client.post('/user/login/', data={'username':'padul','password':'password'})
        self.assertContains(response, 'Wrong password/username')


    def test_user_login_GetRequest(self):

        response = self.client.get('/user/login/')

        # Website exists 
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Welcome Back!')
    

    # INTEGRATION TESTING SignUp -> SignIn
    def test_user_signupLogin(self):

        # Mock input for signup
        data = {
            'username': 'paul',
            'email' : 'paulabijaber@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post('/user/signUp/', data=data)

        # Check if site exists and Databse contains my info
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.get(pk=1).username, 'paul')

        # Check user is logged in
        response = self.client.post('/user/login/', data={'username':'paul','password':'password'})
        self.assertIn('_auth_user_id', self.client.session)


    #####################################################
    #~~~~~~~~~~~~~ TESTS FOR USER_LOGOUT ~~~~~~~~~~~~~~ #
    #####################################################

    # INTEGRATION TESTING SignUp -> SignIn -> SignOut
    def test_user_logout(self):

        # Create User instance in database
        user = User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')
        response = self.client.login(username='paul',password='password')

        # Check if user is logged in and it exists
        self.assertTrue(response)
        self.assertEqual(User.objects.get(pk=1), user)

        # Logout and check we are logged out
        response = self.client.get('/user/logout/')
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, 'Logout')
        self.assertContains(response, 'Signup')

