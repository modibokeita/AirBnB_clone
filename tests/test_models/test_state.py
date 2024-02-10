#!/usr/bin/python3
import os
import models
from models.base_model import BaseModel
from models.state import State
import unittest
"""
User test Module
"""


class TestState(unittest.TestCase):
    """
    set up all possible cases
    for State model
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

    def test_state_attr(self):
        """
        test the state attribute when
        the new instance of user was
        created
        """
        test_state = State()
        self.assertEqual(test_state.name, "")

    def test_state_inherit(self):
        """
        test if the new instance of state was created
        and the instance of user inherit from
        Base model class
        """
        test_inherit = State()
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_str(self):
        """
        test if the state attributes return
        string representation
        """
        test_state = State()
        test_state.name = "Mali"

        state_str = str(test_state)
        self.assertIn("State", state_str)
        self.assertIn("Mali", state_str)

    def test_state_to_dict(self):
        """
        test if the new instance of state
        was created it return a dictoinary
        """
        test_state = State()
        test_state.name = "Mali"
        test_state.save()

        state_dict = test_state.to_dict()
        self.assertEqual(state_dict['name'], "Mali")

    def test_state_id(self):
        """
        test if the states id are
        not the same
        """
        test_state = State()
        state2 = State()

        self.assertNotEqual(test_state.id, state2.id)


if __name__ == "__main__":
    unittest.main()
