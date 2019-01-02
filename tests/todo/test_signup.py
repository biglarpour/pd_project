from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory


class IntroductionRouters(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_empty_post_signup(self):
        """
        We expect the signup page to load when POST empty
        """
        response = self.client.post("/signup/", {})
        self.assertEqual(int(response.status_code), 200)
        self.assertIn('href="/signup/"', str(response.content))

    def test_post_signup(self):
        """
        We expect user to be created and to be redirected to the home page after a successful signup
        """
        response = self.client.post("/signup/", {
            "username": "email@email.com",
            "password1": "MyV0!c3Is",
            "password2": "MyV0!c3Is"})
        user = User.objects.get(username="email@email.com")
        self.assertTrue(user.check_password('MyV0!c3Is'))
        self.assertEqual(response.status_code, 302)

    def test_get_signup(self):
        """
        We expect the signup page to load during a GET call
        """
        response = self.client.get("/signup/")
        self.assertEqual(int(response.status_code), 200)
        self.assertIn('href="/signup/"', str(response.content))
