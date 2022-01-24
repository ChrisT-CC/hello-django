""" form testing """
from django.test import TestCase
from .forms import ItemForm


# Create your tests here.


class TestItemForm(TestCase):
    """
    testing forms
    inherit Testcase and contain all the tests for this form
    """

    def test_item_name_is_required(self):
        """ test item name is required """
        # creates a form instance with an empty "name" field
        form = ItemForm({'name': ''})
        # checks that this field is not valid as it has no name
        self.assertFalse(form.is_valid())
        # checks that there is a 'name' key in the dictionary of form errors
        self.assertIn('name', form.errors.keys())
        # checks if the error message on the "name" key is
        # "This field is required."
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        """ test to ensure the "done" field is not required """
        # create a form instance with a name field of "Test Todo Items"
        form = ItemForm({'name': 'Test Todo Items'})
        # check that this instance is valid even without selecting a
        # "done" status
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        test to ensure that the only fields that are displayed in the form
        are the "name" and "done" fields
        """
        # create an empty form instance
        form = ItemForm()
        # check that the meta fields are equal to "name" and "done"
        self.assertEqual(form.Meta.fields, ['name', 'done'])
