from django.test import TestCase
from django.urls import reverse

USERNAME_JOHN = 'john_lennon'
PASSWORD_JOHN = 'john_password'


class PostCreateTest(TestCase):

    def test_register_and_login_with_new_user(self):
        url = reverse('register')

        # Empty fields in form
        response = self.client.post(url,
                                    {'username': '',
                                     'password': '',
                                     'first_name': '',
                                     'last_name': '',
                                     'email': ''})
        self.assertFormError(response, 'form', 'username',
                             'This field is required.')
        self.assertFormError(response, 'form', 'password',
                             'This field is required.')

        # Register User
        response = self.client.post(url,
                                    {'username': USERNAME_JOHN,
                                     'password': PASSWORD_JOHN,
                                     'first_name': 'John',
                                     'last_name': 'Lennon',
                                     'email': 'lennon@thebeatles.com'})
        self.assertRedirects(response, reverse('login'))

        # Log in newly registered user
        user_logged_in = self.client.login(username=USERNAME_JOHN,
                                           password=PASSWORD_JOHN)
        self.assertTrue(user_logged_in)

        url = reverse('blog:home')
        response = self.client.get(url)
        self.assertTrue(response.context['request'].user.is_authenticated)
