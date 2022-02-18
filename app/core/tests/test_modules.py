from logging import raiseExceptions
from unittest.case import _AssertRaisesContext
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """This test is to create a user with email and validate it"""
        email = 'test@geetha.com'
        password = 'test123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalise(self):
        """Tests the email for new user """
        email ="test@GEETHA.COM"
        user = get_user_model().objects.create_user(email=email, password='123456')
        self.assertEqual(email.lower(), user.email)
    
    def test_super_user(self):
        """Tests the super_user created or not"""
        user = get_user_model().objects.create_superuser(email="geeth@gmail.com", password="122344")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
