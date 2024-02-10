#!/usr/bin/python3

"""
city test Module
"""
from models.city import City
from models.base_model import BaseModel
import models
import os
import unittest


class TestCity(unittest.TestCase):
    """
    set up all possible cases for
    testing City module
    """
    test_file = "test_file.json"

    
    def setUp(sef):
        """
        create a temporary file for
        saving the data of city
        """
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """
        that method removes the file
        after the test is done
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_city_attr(self):
        """
        test the city attributes when the
        new of city was created
        """
        test_city = City()
        self.assertEqual(test_city.name, "")
        self.assertEqual(test_city.state_id, "")

    def test_user_inherit(self):
        """
        test if the new instance of user was created
        and the instance of city inherit from
        Base model class
        """
        test_inherit = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_user_str(self):
        """
        test if the city attributes return
        string representation
        """
        test_city = City()
        test_city.name = "Bamako"
        test_city.state_id = "Bko223"

        city_str = str(test_city)
        self.assertIn("City",test_city)
        self.assertIn("Bamako", test_city)
        self.assertIn("Bko223", test_city)

    def test_city_to_dict(self):
        """
        test if the new instance of city
        was created it return a dictoinary
        """
        test_city = City()
        test_city.name = "Bamako"
        test_city.state_id = "Bko223"
        test_city.save()

        city_dict = test_user.to_dict()

        self.assertEqual(city_dict['name'], "Bamako")
        self.assertEqual(city_dict['state_id'], "Bko223")

    def test_city_id(self):
        """
        test if the citys id are
        not the same
        """
        test_city = City()
        city2 = City()

        self.assertNotEqual(test_city.id, city2.id)


if __name__ == "__main__":
    unittest.main()
