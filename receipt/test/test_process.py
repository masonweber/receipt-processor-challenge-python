from django.test import RequestFactory, TestCase

#from receipt.views import process


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="jacob", email="jacob@…", password="top_secret"
        )

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get("/customer/details")

       

        # Test my_view() as if it were deployed at /customer/details
        response = 
        # Use this syntax for class-based views.
        response = MyView.as_view()(request)
        self.assertEqual(response.status_code, 200)