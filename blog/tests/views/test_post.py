from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models.post import Post

USERNAME_JOHN = 'john_lennon'
PASSWORD_JOHN = 'john_password'
USERNAME_GEORGE = 'george_harrison'
PASSWORD_GEORGE = 'george_password'


class PostViewTest(TestCase):

    def setUp(self):
        self.test_user_john = User.objects.create_user(
            USERNAME_JOHN, 'lennon@thebeatles.com', PASSWORD_JOHN)
        self.test_user_george = User.objects.create_user(
            USERNAME_GEORGE, 'lennon@thebeatles.com', PASSWORD_GEORGE)
        self.test_post_john = Post.objects.create(user=self.test_user_john,
                                                  title='Title 1',
                                                  body='Lorem ipsum')
        self.url = reverse('blog:post', kwargs={'pk': self.test_post_john.id})

    def test_viewing_post_by_author(self):
        self.client.login(username=USERNAME_JOHN, password=PASSWORD_JOHN)
        response = self.client.get(self.url)
        self.assertContains(response, 'Update</button>')
        self.assertContains(response, 'Delete</button>')

    def test_viewing_post_by_non_author(self):
        self.client.login(username=USERNAME_GEORGE, password=PASSWORD_GEORGE)
        response = self.client.get(self.url)
        self.assertNotContains(response, 'Update</button>')
        self.assertNotContains(response, 'Delete</button>')


class PostCreateTest(TestCase):

    def setUp(self):
        self.test_user_john = User.objects.create_user(
            USERNAME_JOHN, 'lennon@thebeatles.com', PASSWORD_JOHN)
        self.url = reverse('blog:create_post')

    def test_create_post_by_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertRedirects(response,
                             f'{reverse("login")}?next={self.url}')

    def test_create_post_by_logged_user(self):
        self.client.login(username=USERNAME_JOHN, password=PASSWORD_JOHN)

        # Empty fields in form
        response = self.client.post(self.url, {'title': '', 'body': ''})
        self.assertFormError(response, 'form', 'title',
                             'This field is required.')
        self.assertFormError(response, 'form', 'body',
                             'This field is required.')

        # Non-empty fields in form
        response = self.client.post(self.url,
                                    {'title': 'Title 3', 'body': 'Lorem ipsum'})
        self.assertRedirects(response, reverse('blog:post', kwargs={'pk': 1}))


class PostUpdateTest(TestCase):

    def setUp(self):
        self.test_user_john = User.objects.create_user(
            USERNAME_JOHN, 'lennon@thebeatles.com', PASSWORD_JOHN)
        self.test_user_george = User.objects.create_user(
            USERNAME_GEORGE, 'lennon@thebeatles.com', PASSWORD_GEORGE)
        self.test_post_john = Post.objects.create(user=self.test_user_john,
                                                  title='Title 1',
                                                  body='Lorem ipsum')
        self.url = reverse('blog:update_post',
                           kwargs={'pk': self.test_post_john.id})

    def test_update_post_by_anonymous_user(self):
        response = self.client.post(self.url,
                                    {'title': 'Title 3', 'body': 'Lorem ipsum'})
        self.assertRedirects(response,
                             f'{reverse("login")}?next={self.url}')

    def test_update_post_by_author(self):
        self.client.login(username=USERNAME_JOHN, password=PASSWORD_JOHN)

        # Empty fields in form
        response = self.client.post(self.url, {'title': '', 'body': ''})
        self.assertFormError(response, 'form', 'title',
                             'This field is required.')
        self.assertFormError(response, 'form', 'body',
                             'This field is required.')

        # Non-empty fields in form
        response = self.client.post(self.url,
                                    {'title': 'Title 3', 'body': 'Lorem ipsum'})
        self.assertRedirects(response,
                             reverse('blog:post',
                                     kwargs={'pk': self.test_post_john.id}))

    def test_update_post_by_non_author(self):
        self.client.login(username=USERNAME_GEORGE, password=PASSWORD_GEORGE)
        response = self.client.post(self.url,
                                    {'title': 'Title 3', 'body': 'Lorem ipsum'})
        self.assertEqual(response.status_code, 403)


class PostDeleteTest(TestCase):

    def setUp(self):
        self.test_user_john = User.objects.create_user(
            USERNAME_JOHN, 'lennon@thebeatles.com', PASSWORD_JOHN)
        self.test_user_george = User.objects.create_user(
            USERNAME_GEORGE, 'lennon@thebeatles.com', PASSWORD_GEORGE)
        self.test_post_john = Post.objects.create(user=self.test_user_john,
                                                  title='Title 1',
                                                  body='Lorem ipsum')
        self.url = reverse('blog:delete_post',
                           kwargs={'pk': self.test_post_john.id})

    def test_delete_post_by_anonymous_user(self):
        response = self.client.post(self.url)
        self.assertRedirects(response,
                             f'{reverse("login")}?next={self.url}')

    def test_delete_post_by_author(self):
        self.client.login(username=USERNAME_JOHN, password=PASSWORD_JOHN)
        response = self.client.post(self.url)
        self.assertRedirects(response, reverse('blog:home'))

    def test_delete_post_by_non_author(self):
        self.client.login(username=USERNAME_GEORGE, password=PASSWORD_GEORGE)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 403)
