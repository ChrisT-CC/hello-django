""" testing views """
from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    """
    check that the views return a successful HTTP response 
    check that they're using the proper templates
    check what they can do: adding, toggling and deleting items
    """
    def test_get_todo_list(self):
        """ test getting the "todo_list" """
        # save the homepage instance as response
        response = self.client.get('/')
        # check that the response code is 200 (success)
        self.assertEqual(response.status_code, 200)
        # check that the template used is "todo/todo_list.html"
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """ test getting the "add_item" page """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """ test getting the "edit_item" page """
        # create an Item Object
        item = Item.objects.create(name='Test Todo Item')
        # save the response for that item
        response = self.client.get(f'/edit/{item.id}')
        # assert this item response code is 200
        self.assertEqual(response.status_code, 200)
        # assert the template used is "edit_item.html"
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ test that we can add an item using the "add_item" view """
        # create a new item
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # check it redirects to the home page
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """ test that we can delete an item using the "delete_item" view """
        # create a new item object instance
        item = Item.objects.create(name='Test Todo Item')
        # delete this item
        response = self.client.get(f'/delete/{item.id}')
        # assert that it redirects to the home page
        self.assertRedirects(response, '/')
        # try to return the item from the DB using filter and the item_id
        existing_items = Item.objects.filter(id=item.id)
        # check the length of existing_items = 0
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """ test we can toggle an item using the "toggle_item" view """
        # create a new item object instance with done=True
        item = Item.objects.create(name='Test Todo Item', done=True)
        # toggle this item so done=False
        response = self.client.get(f'/toggle/{item.id}')
        # assert that it redirects to the home page
        self.assertRedirects(response, '/')
        # get the item again and save as updated_item
        updated_item = Item.objects.get(id=item.id)
        # check the done status is False
        self.assertFalse(updated_item.done)
