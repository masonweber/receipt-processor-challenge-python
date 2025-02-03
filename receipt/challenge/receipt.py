import uuid
import math
import re

class Receipt:
    def __init__(self, id, retailer, purchase_date, purchase_time, items, total):
        self._id = id #new uuid/endpoint submit with str(uuid.uuid4()) 
        self._retailer = retailer
        self._purchase_date = purchase_date
        self._purchase_time = purchase_time
        self._items = items
        self._total = total
        self._points = None

    def get_points(self):
        if self._points is None:
            print("calculating points")
            self._points = 0
            #Retailer name
            self._points += len(re.findall("[a-zA-Z0-9]", self._retailer)) #filter out whitespace and special chars
            print(self._points)

            #Total is dollar
            if self._total[-2:] == "00": #compare string for cents
                self._points += 50
            print(self._points)

            #Total is *0.25
            if int(self._total[-2:]) % 25 == 0: #parse cents for mod check
                self._points += 25
            print(self._points)

            #Total items
            self._points += 5 * (len(self._items) // 2) #floor division for groups of 2
            print(self._points)

            #Item name length
            for item in self._items: #loop items, order does not matter
                if len(item["short_description"].strip()) % 3 == 0:  #trim item name
                    self._points += math.ceil(float(item["price"]) * 0.2) #cast to float as needed
                    print(self._points)

            #Purchase Date
            if int(self._purchase_date[9:10]) % 2 == 1: #grab day from yyyy-MM-dd format, indicies 9&10
                self._points += 6
            print(self._points)

            #Purchase Time
            if (self._purchase_time > "14:00") & (self._purchase_time < "16:00"): #just use lexographical sort here, reqirements exclude on the hour             
                self._points += 10
            print(self._points)
            
        return self._points