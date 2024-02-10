#!/usr/bin/python3
import os
import models
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
"""
Amenity test Module
"""


class TestAmenity(unittest.TestCase):
    """
    set up all possible cases
    for Amenity model
    """
    test_file = "test_file.json"

    def setUpt(self):
        """
        create a temporary file for
        amenity data to be able be saved
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

    def test_amenity_attr(self):
        """
        test the amenity attribute when
        the new instance of amenity was
        created
        """
        test_amenity = Amenity()
        self.assertEqual(test_amenity.name, "")

    def test_amenity_inherit(self):
        """
        test if the new instance of amenity was created
        and the instance of amenity inherit from
        Base model class
        """
        test_inherit = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_str(self):
        """
        test if the amenity attributes return
        string representation
        """
        test_amenity = Amenity()
        test_amenity.name = "Cool"

        amenity_str = str(test_amenity)
        self.assertIn("Amenity", amenity_str)
        self.assertIn("Cool", amenity_str)

    def test_amenity_to_dict(self):
        """
        test if the new instance of amenity
        was created it return a dictoinary
        """
        test_amenity = Amenity()
        test_amenity.name = "Cool"
        test_amenity.save()

        amenity_dict = test_amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "Cool")

    def test_Amenity_id(self):
        """
        test if the amenity id are
        not the same
        """
        test_amenity = Amenity()
        amenitye2 = Amenity()

        self.assertNotEqual(test_amenity.id, amenity2.id)


if __name__ == "__main__":
    unittest.main()
