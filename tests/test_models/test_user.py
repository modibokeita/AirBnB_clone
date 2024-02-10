#!/usr/bin/python3
import os
import models
from models.base_model import BaseModel
from models.user import User
import unittest
"""
User test Module
"""


class TestUser(unittest.TestCase):
    """
    set up all possible cases
    for User model
    """
    test_file = "test_file.json"

    def setUpt(self):
        """
        create a temporary file for
        user data to be able be saved
        on file
        """
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        the method to remove the temporary
        file after the test is donee
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_use_attr(self):
        """
        test the user attribute when
        the new instance of user was
        created
        """
        test_user = User()
        self.assertEqual(test_user.email, "")
        self.assertEqual(test_user.password, "")
        self.assertEqual(test_user.first_name, "")
        self.assertEqual(test_user.last_name, "")

    def test_user_inherit(self):
        """
        test if the new instance of user was created
        and the instance of user inherit from
        Base model class
        """
        test_inherit = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_str(self):
        """
        test if the user attributes return
        string representation
        """
        test_user = User()
        test_user.email = "modibokeita9390@gmail.com"
        test_user.password = "password1234"
        test_user.first_name = "Modibo"
        test_user.last_name = "Keita"

        users_str = str(test_user)
        self.assertIn("User", users_str)
        self.assertIn("modibokeita9390@gmail.com", users_str)
        self.assertIn("Modibo", users_str)
        self.assertIn("Keita", users_str)

    def test_user_to_dict(self):
        """
        test if the new instance of user
        was created it return a dictoinary
        """
        test_user = User()
        test_user.email = "modibokeita9390@gmail.com"
        test_user.first_name = "Modibo"
        test_user.last_name = "Keita"
        test_user.save()

        user_dict = test_user.to_dict()

        self.assertEqual(user_dict['email'], "modibokeita9390@gmail.com")
        self.assertEqual(user_dict['first_name'], "Modibo")
        self.assertEqual(user_dict['last_name'], "Keita")

    def test_user_id(self):
        """
        test if the users id are
        not the same
        """
        test_user = User()
        user2 = User()

        self.assertNotEqual(test_user.id, user2.id)


if __name__ == "__main__":
    unittest.main()
