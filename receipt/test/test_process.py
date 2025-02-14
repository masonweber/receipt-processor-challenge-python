from django.test import RequestFactory, TestCase
from challenge import process

class ProcessTest(TestCase):
    def test_score(self):
        """
        score returns error before receipt is submitted, then returns points message after ingesting
        """
        self.assertRaises(KeyError, process.score, "95e8f5b8-992a-466b-8cf7-d235ddd055c4")
        process.ingest("95e8f5b8-992a-466b-8cf7-d235ddd055c4", {"retailer": "Walgreens","purchaseDate": "2022-01-02","purchaseTime": "08:13","total": "2.65",
            "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"},{"shortDescription": "Dasani", "price": "1.40"}]})
        self.assertEqual(process.score("95e8f5b8-992a-466b-8cf7-d235ddd055c4"), 15)

    def test_injest(self):
        """
        injesting a new receipt with already existing ID will overwrite
        """
        process.ingest("1", {"retailer": "Walgreens","purchaseDate": "2022-01-02","purchaseTime": "08:13","total": "2.65",
            "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"},{"shortDescription": "Dasani", "price": "1.40"}]})
        self.assertEqual(process.score("1"), 15)
        process.ingest("1", {"retailer": "Target","purchaseDate": "2022-01-02","purchaseTime": "13:13","total": "1.25",
            "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}]})
        self.assertEqual(process.score("1"), 31)