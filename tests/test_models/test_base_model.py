#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
"""
Test base Model
"""


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """
        test for init method
        it every instance to see if it will
        the expecteb result
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """
        test for save method, it will
        checks if actually the current update and
        the initial update are not equal
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at

        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """
        test for to_dict method that will checks
        if the expected result is return from
        the method
        """
        my_model = BaseModel()

        my_model_dict = my_model.to_dict()

        self.assertIsInstance(my_model_dict, dict)

        created_date = my_model.created_at.isoformat()
        updated_date = my_model.updated_at.isoformat()
        self.assertEqual(my_model_dict["__class__"], "BaseModel")
        self.assertEqual(my_model_dict["id"], my_model.id)
        self.assertEqual(my_model_dict["created_at"], created_date)
        self.assertEqual(my_model_dict["updated_at"], updated_date)

    def test_str(self):
        """
        test for str method that checks for class
        name and make sure if that return a dict
        amd an id
        """
        my_model = BaseModel()
        self.assertTrue(str(my_model).startswith("[BaseModel]"))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == '__main__':
    unittest.main()
