from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from blog.models.post import Post
from blog.views.home import NUM_OF_POSTS

USERNAME = 'john_lennon'
PASSWORD = 'john_password'


class HomeViewTest(TestCase):
    fixtures = ['users', 'posts', 'comments']

    def setUp(self):
        self.test_user = User.objects.create_user(USERNAME,
                                                  'lennon@thebeatles.com',
                                                  PASSWORD)
        self.test_user.first_name = 'John'
        self.test_user.last_name = 'Lennon'
        self.test_user.save()
        Post.objects.create(user=self.test_user, title='Title 1',
                            body='Lorem ipsum')
        Post.objects.create(user=self.test_user, title='Title 2',
                            body='Lorem ipsum')
        Post.objects.create(user=self.test_user, title='Title 3',
                            body='Lorem ipsum')

    def test_home_page_all_posts(self):
        url = reverse('blog:home')
        response = self.client.get(url)
        posts = Post.objects.all().order_by('-pub_date')[:NUM_OF_POSTS]
        self.assertQuerysetEqual(response.context['posts'], posts)

    def test_home_page_anonymous_user_buttons(self):
        url = reverse('blog:home')
        response = self.client.get(url)
        self.assertContains(response, 'Registration')
        self.assertContains(response, 'Login')
        self.assertNotContains(response, 'New Post')
        self.assertNotContains(response, 'Sign Out')

    def test_home_page_logged_user_buttons(self):
        self.client.login(username=USERNAME, password=PASSWORD)
        url = reverse('blog:home')
        response = self.client.get(url)
        self.assertNotContains(response, 'Registration')
        self.assertNotContains(response, 'Login')
        self.assertContains(response, 'New Post')
        self.assertContains(response, 'Sign Out')

    def test_user_posts_page_only_users_posts(self):
        # /blog/john_lennon
        url = reverse('blog:user_posts',
                      kwargs={'username': self.test_user.username})
        response = self.client.get(url)
        posts = Post.objects.filter(
            user=self.test_user).order_by('-pub_date')[:NUM_OF_POSTS]
        self.assertQuerysetEqual(response.context['posts'], posts)
        self.assertContains(response, self.test_user.first_name)
        self.assertContains(response, self.test_user.last_name)
        self.assertEqual(response.context['first_name'],
                         self.test_user.first_name)
        self.assertEqual(response.context['last_name'],
                         self.test_user.last_name)
