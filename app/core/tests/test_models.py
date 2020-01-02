from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # creating new user email address and password
        email = 'abc@gmail.com'
        password = 'abc123'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))



    def test_new_user_email_normalized(self):
        # test the new user email is normalized
        email = 'abc@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        # test creating user with no email address raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_new_superuser(self):
        # test to create a new superuser
        user = get_user_model().objects.create_superuser('abc@gmail.com', 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
