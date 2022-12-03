from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models.post import Post

USERNAME_JOHN = 'john_lennon'
PASSWORD_JOHN = 'john_password'


class PostCreateTest(TestCase):

    def setUp(self):
        self.test_user_john = User.objects.create_user(
            USERNAME_JOHN, 'lennon@thebeatles.com', PASSWORD_JOHN)
        self.test_post_john = Post.objects.create(user=self.test_user_john,
                                                  title='Title 1',
                                                  body='Lorem ipsum')
        self.url = reverse('blog:create_comment',
                           kwargs={'pk': self.test_post_john.id})

    def test_create_comment_by_anonymous_user(self):
        response = self.client.get(self.url)
        self.assertRedirects(response,
                             f'{reverse("login")}?next={self.url}')

    def test_create_comment_by_logged_user(self):
        self.client.login(username=USERNAME_JOHN, password=PASSWORD_JOHN)

        # Empty fields in form
        response = self.client.post(self.url, {'body': ''})
        self.assertFormError(response, 'form', 'body',
                             'This field is required.')

        # Non-empty fields in form
        response = self.client.post(self.url, {'body': 'Lorem ipsum'})
        self.assertRedirects(response, reverse('blog:post', kwargs={
            'pk': self.test_post_john.id}))
