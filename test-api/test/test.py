import sys
import os

from fastapi import HTTPException

# Get the absolute path of the src directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
import src.endpoints.item as item_endpoint

class TestCases(unittest.TestCase):
    def test_get_items(self):
        """
        Does /get items return any items?
        """
        items = item_endpoint.get_items()
        self.assertGreater(len(items), 0)
    
    def test_get_item(self):
        """
        Does /item/id/{input} return an item?
        """
        item = item_endpoint.get_item(0)
        self.assertIsNotNone(item)

    def test_create_item(self):
        """
        Can a item be created?
        """
        response = item_endpoint.create_item(
            name="banana",
            price=1,
            quantity=1)
        self.assertEqual(response['status'], 201)
        self.assertEqual(response['message'], "Added banana to the list of items")        

    def test_create_item_no_name(self):
        """
        Does "400 BAD REQUEST" return if no name is specified?
        """
        with self.assertRaises(HTTPException) as context:
            item_endpoint.create_item(name="", price=1, quantity=1)

        self.assertEqual(context.exception.status_code, 400)

    def test_update_item(self):
        """
        Can a item's properties be changed?
        """
        reponse = item_endpoint.update_item(
            item_id=0,
            name="banana",
            price=25,
            quantity=5)
        
        self.assertEqual(reponse['status'], 200) 
        self.assertEqual(reponse['message'], "Item '0' was successfully updated!")
    
    def test_update_item_no_id(self):
        with self.assertRaises(HTTPException) as context:
            item_endpoint.update_item(
            item_id=None,
            name="banana",
            price=25,
            quantity=5)
        
        self.assertEqual(
            context.exception.detail,
            "id of item was not specified")
    
    def test_update_item_no_price(self):
        with self.assertRaises(HTTPException) as context:
            item_endpoint.update_item(
            item_id=0,
            name=None,
            price=None,
            quantity=None)
        
        self.assertEqual(
            context.exception.detail,
            "no new values of item's properties was specified")

if __name__ == '__main__':
    unittest.main()