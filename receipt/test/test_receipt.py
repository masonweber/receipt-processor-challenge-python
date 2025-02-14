from django.test import TestCase
from challenge.receipt import Receipt

class ReceiptTests(TestCase):
    def test_morning_receipt(self):
        """
        receipt using example morning-receipt.json
        """
        morning_receipt = Receipt("f87beab2-79ab-4986-b427-ff60c1d04100", "Walgreens", "2022-01-02", "08:13", 
            [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"},{"shortDescription": "Dasani", "price": "1.40"}], "2.65")
        self.assertEqual(morning_receipt.get_points(), 15)

    def test_simple_receipt(self):
        """
        receipt using example simple-receipt.json
        """
        simple_receipt = Receipt("f87beab2-79ab-4986-b427-ff60c1d04100", "Target", "2022-01-02", "13:13", 
            [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}], "1.25")
        self.assertEqual(simple_receipt.get_points(), 31)
    def test_empty_receipt_errors(self):
        """
        receipt constructed with no data will return a type error with get_points
        """
        null_receipt = Receipt(None, None, None, None, None, None)
        self.assertRaises(TypeError, null_receipt.get_points)

    def test_blank_retailer_no_items(self):
        """
        receipt with empty retailer and 0 items with chosen date and time can return 0 points
        """
        blank_receipt = Receipt("83e58a34-2a09-4da1-872f-d7751eed1b8d","", "2022-02-02", "09:00", [], "0.01")
        self.assertEqual(blank_receipt.get_points(), 0)

    def test_retail_name(self):
        """
        receipt with alphanumeric characters, all worth points
        """
        name_receipt = Receipt("f33687f0-0988-4b4c-9654-c213ae298f13","Companion", "2022-02-02", "09:00", [], "0.01")
        self.assertEqual(name_receipt.get_points(), 9)
        

    def test_retail_name_with_special_chars(self):
        """
        receipt with mix of alphanumeric, space, and special characters, will return only alphanumeric count points
        """
        mixed_name_receipt = Receipt("3c7dd3a7-b6d7-43a7-8510-894a7236ea60","Will's Guitar Haven", "2022-02-02", "09:00", [], "0.01")
        self.assertEqual(mixed_name_receipt.get_points(), 16)
    
    def test_retail_name_only_special_chars(self):
        """
        receipt with special characters and spaces only to return 0 points
        """
        special_name_receipt = Receipt("63b5e032-9d1b-4885-90b9-2931187ed723","$&$' @", "2022-02-02", "09:00", [], "0.01")
        self.assertEqual(special_name_receipt.get_points(), 0)

    def test_total_whole_dollar(self):
        """
        receipt with total ending in .00
        """
        whole_number_receipt = Receipt("cc73a08a-2e39-4dd4-a9c5-934307edb0e0","", "2022-02-02", "09:00", [], "10.00")
        self.assertEqual(whole_number_receipt.get_points(), 75)
    
    def test_total_quarter(self):
        """
        receipt with total ending in .25
        """
        quarter_number_receipt = Receipt("64dcbf71-3082-40ac-bd8e-4eb073ead4f6","", "2022-02-02", "09:00", [], "0.25")
        self.assertEqual(quarter_number_receipt.get_points(), 25)

    def test_items_even(self):
        """
        receipt with an even number of items >0
        """
        even_item_receipt = Receipt("8cd92f9c-5214-4cc8-9651-d88c97a75695","", "2022-02-02", "09:00", [{"shortDescription":"item1", "price":"1.23"}
            ,{"shortDescription":"item2", "price":"2.34"}], "0.01")
        self.assertEqual(even_item_receipt.get_points(), 5)

    def test_items_odd(self):
        """
        receipt with an odd number of total items
        """
        odd_item_receipt = Receipt("eea3fed9-fd6c-4bd7-a55d-ea2adc777e75","", "2022-02-02", "09:00", [{"shortDescription":"item1", "price":"1.23"}
            ,{"shortDescription":"item2", "price":"2.34"},{"shortDescription":"item3", "price":"3.45"}], "0.01")
        self.assertEqual(odd_item_receipt.get_points(), 5)
    
    def test_item_name_length(self):
        """
        receipt with one item with description length divisible by 3
        """
        item_name_receipt = Receipt("dd762200-7006-469b-9a83-f94576c7bc27","", "2022-02-02", "09:00", [{"shortDescription":"Delicous Magica Seeds", "price":"10.00"}], "0.01")
        self.assertEqual(item_name_receipt.get_points(), 2)
    
    def test_purchase_date(self):
        """
        receipt with purchase date on odd day
        """
        odd_date_receipt = Receipt("927ff181-bdb5-4c88-ac56-ffb87b6cf337","", "2021-01-01", "09:00", [], "0.01")
        self.assertEqual(odd_date_receipt.get_points(), 6)

    def test_purchase_time(self):
        """
        receipt with purchase time between 14h and 16h
        """
        afternoon_receipt = Receipt("927ff181-bdb5-4c88-ac56-ffb87b6cf337","", "2021-02-04", "15:00", [], "0.01")
        self.assertEqual(afternoon_receipt.get_points(), 10)