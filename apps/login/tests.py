from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from .views import user_login, user_logout


class UserLoginTests(TestCase):

    # create pseudo user
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="joko", email="kko@gmail", password="top")

    # test if user is known
    def test_user_login_known(self):
        request = self.factory.get('/profile/')
        request.user = self.user
        response = user_login(request)
        # self.assertTemplateUsed(response, 'base_profile.html')
        self.assertEqual(response.status_code, 302)
        # self.assertContains(response, 'joko')

    # test if user is anonymous
    def test_user_login_anonymous(self):
        request = self.factory.get('/profile/')
        request.user = AnonymousUser()
        response = user_login(request)
        # self.assertTemplateUsed(response, 'base_profile.html')
        self.assertEqual(response.status_code, 200)

    # test if user is active
    def test_user_login_active(self):
        request = self.factory.get('/profile/')
        request.user = self.user
        # request.user = AnonymousUser()
        if request.user.is_active:
            response = user_login(request)
            # self.assertTemplateUsed(response, 'profile.html')
            self.assertEqual(response.status_code, 302)
        else:
            response = user_login(request)
            # self.assertTemplateUsed(response, 'login.html')
            self.assertNotEqual(response.status_code, 302)


class UserLogoutTests(TestCase):

    # create pseudo user
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="joko", email="kko@gmail", password="top")

    # if user is anonymous
    def test_user_logout_anonymous(self):
        request = self.factory.get('/login/')
        request.user = AnonymousUser()
        response = user_logout(request)
        # print(response.status_code)
        self.assertEqual(response.status_code, 302)
