from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuItemTest(TestCase):

    def test_adding_item(self):
        item = Menu.objects.create(title="Ice Cream", price=80, inventory=100)
        self.assertEqual(str(item), "Ice Cream : 80")