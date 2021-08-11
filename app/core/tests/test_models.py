from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a user with email and password is successful."""

        email = "me@me.com"
        password = "changeme"
        User = get_user_model()
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_user_email_normalized(self):
        """Creates a user with a normalized email - domain in lower case"""
        email = "me@ME.COM"
        User = get_user_model()
        user = User.objects.create_user(email=email, password="mememe")

        self.assertEqual(user.email, "me@me.com")

    def test_new_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "password")

    def test_new_supperuser(self):
        User = get_user_model()
        user = User.objects.create_superuser("admin@me.com", "super_secret")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
