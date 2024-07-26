from django.contrib.auth import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse("users:register"), data={
            "username": "Marufjon",
            "first_name": "Maruf",
            "last_name": "Ibragimov",
            "email": "ibragimovmaruf1108@gmail.com",
            "password": "somepassword"
        })

        user = CustomUser.objects.get(username="Marufjon")

        self.assertEqual(user.first_name, "Maruf")
        self.assertEqual(user.last_name, "Ibragimov")
        self.assertEqual(user.email, "ibragimovmaruf1108@gmail.com")
        self.assertNotEqual(user.password, "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "first_name": "Maruf",
                "email": "ibragimovmaruf1108@gmail.com"
            }
        )

        user_account = CustomUser.objects.count()

        self.assertEqual(user_account, 0)
        self.assertFormError(response, "form", "username", "This field is required.")
        self.assertFormError(response, "form", "password", "This field is required.")

    def test_invalid_email(self):
        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "Marufjon",
                "first_name": "Maruf",
                "last_name": "Ibragimov",
                "email": "ibragimovmaruf1108@@gmail.com",
                "password": "somepassword"
            }
        )

        user_account = CustomUser.objects.count()

        self.assertEqual(user_account, 0)
        self.assertFormError(response, "form", "email", "Enter a valid email address.")

    def test_unique_username(self):
        user = CustomUser.objects.create(username="Marufjon", first_name="Maruf")
        user.set_password("somepass")
        user.save()

        response = self.client.post(
            reverse("users:register"),
            data={
                "username": "Marufjon",
                "first_name": "Maruf",
                "last_name": "Ibragimov",
                "email": "ibragimovmaruf1108@gmail.com",
                "password": "somepassword"
            }
        )

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)
        self.assertFormError(response, "form", "username", "A user with that username already exists.")


class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create(username='Maruf', first_name='Maruf')
        self.db_user.set_password('somepass')
        self.db_user.save()

    def test_successful_login(self):
        self.client.post(
            reverse('users:login'),
            data={
                'username': "Maruf",
                'password': 'somepass',
            }
        )

        user = get_user(self.client)

        self.assertTrue(user.is_authenticated)

    def test_wrong_credentials(self):
        self.client.post(
            reverse('users:login'),
            data={
                'username': "wrong-username",
                'password': 'somepass',
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        self.client.post(
            reverse('users:login'),
            data={
                'username': "Maruf",
                'password': 'wrong-password',
            }
        )

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username="Maruf", password="somepass")

        self.client.get(reverse("users:logout"))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)


class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.url, reverse("users:login") + "?next=/users/profile/")

    def test_profile_details(self):
        user = CustomUser.objects.create(
            username="Marufjon", first_name="Maruf", last_name="Ibragimov", email="ibragimovmaruf1108@gmail.com",
        )
        user.set_password("somepass")
        user.save()

        self.client.login(username="Marufjon", password="somepass")

        response = self.client.get(reverse("users:profile"))

        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_update_profile(self):
        user = CustomUser.objects.create(
            username="Marufjon", first_name="Maruf", last_name="Ibragimov", email="ibragimovmaruf1108@gmail.com",
        )
        user.set_password("somepass")
        user.save()

        self.client.login(username="Marufjon", password="somepass")

        response = self.client.post(
            reverse("users:profile-edit"),
            data={
                "username": "Marufjon",
                "first_name": "Maruf",
                "last_name": "Johnson",
                "email": "semiz@gmail.com"
            }
        )

        # user = User.objects.get(pk=user.pk)

        user.refresh_from_db()

        self.assertEqual(user.last_name, "Johnson")
        self.assertEqual(user.email, "semiz@gmail.com")
        self.assertEqual(response.url, reverse("users:profile"))