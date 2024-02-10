#!/usr/bin/python3
import os
import models
from models.base_model import BaseModel
from models.place import Place
import unittest
"""
Place test Module
"""


class TestPlace(unittest.TestCase):
    """
    set up all possible cases
    for Place model
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

    def test_place_attr(self):
        """
        test the place attribute when
        the new instance of user was
        created
        """
        test_place = Place()
        self.assertEqual(test_place.city_id, "")
        self.assertEqual(test_place.user_id, "")
        self.assertEqual(test_place.name, "")
        self.assertEqual(test_place.description, "")
        self.assertEqual(test_place.number_rooms, 0)
        self.assertEqual(test_place.number_bathrooms, 0)
        self.assertEqual(test_place.max_guest, 0)
        self.assertEqual(test_place.latitude, 0.0)
        self.assertEqual(test_place.longitude, 0.0)
        self.assertEqual(test_place.amenity_ids, [])

    def test_place_inherit(self):
        """
        test if the new instance of place was created
        and the instance of user inherit from
        Base model class
        """
        test_inherit = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_Place_str(self):
        """
        test if the place attributes return
        string representation
        """
        test_place = Place()
        test_place.city_id = "Bk"
        test_place.user_id = "p1234"
        test_place.name = "Kati"
        test_place.description = "Kati kadi trop"
        test_place.number_rooms = 2
        test_place.number_bathrooms = 1
        test_place.max_guest = 1
        test_place.latitude = 358.52
        test_place.longitude = 368.50
        test_place.amenity_ids = ["ps1", "ps2", "ps3"]

        places_str = str(test_place)
        self.assertIn("Place", places_str)
        self.assertIn("Bk", places_str)
        self.assertIn("Kati", places_str)
        self.assertIn("Kati kadi trop", places_str)
        self.assertIn(2, places_str)
        self.assertIn(1, places_str)
        self.assertIn(1, places_str)
        self.assertIn(358.52, places_str)
        self.assertIn(368.50, places_str)
        self.assertIn(["ps1", "ps2", "ps3"], places_str)

    def test_place_to_dict(self):
        """
        test if the new instance of place
        was created it return a dictoinary
        """
        test_plce = Place()
        test_place.city_id = "Bk"
        test_place.user_id = "p1234"
        test_place.name = "Kati"
        test_place.description = "Kati kadi trop"
        test_place.number_rooms = 2
        test_place.number_bathrooms = 1
        test_place.max_guest = 1
        test_place.latitude = 358.52
        test_place.longitude = 368.50
        test_place.amenity_ids = ["ps1", "ps2", "ps3"]
        test_place.save()

        plce_dict = test_place.to_dict()

        self.assertEqual(plce_dict['city+id'], "Bko")
        self.assertEqual(place_dict['user_id'], "p1234")
        self.assertEqual(place_dict['name'], "Kati")
        self.assertEqual(place_dict['description'], "Kati kadi trop")
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 1)
        self.assertEqual(place_dict['latitude'], 358.52)
        self.assertEqual(place_dict['longitude'], 368.50)
        self.assertEqual(place_dict['amenity_ids'], ["ps1", "ps2", "ps3"])

    def test_place_id(self):
        """
        test if the places id are
        not the same
        """
        test_place = Place()
        place2 = Place()

        self.assertNotEqual(test_place.id, place2.id)


if __name__ == "__main__":
    unittest.main()
