""" model testing """
from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModels(TestCase):
    """ contains all the tests for the model """
    def test_get_todo_list(self):
        """
        test that the todo items will be created by default with the "done"
        status of false
        """
        # create a new item instance
        item = Item.objects.create(name='Test Todo Item')
        # check that item.done is False
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        """ test the string method of the item model """
        # create a new item instance
        item = Item.objects.create(name='Test Todo Item')
        # assert the item's string is "Test Todo Item"
        self.assertEqual(str(item), 'Test Todo Item')

