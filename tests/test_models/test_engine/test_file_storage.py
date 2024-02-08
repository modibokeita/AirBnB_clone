#!/usr/bin/python3

import unittest
import os
import models

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstance(unittest.TestCase):

    """
    Test the Instatiation of
    file storage
    """
    def test_fileStorage_no_arg(self):

        """
        Test the file storage with no
        arguments
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_fileStorage_with_arg(self):
        """
        test the file storage if there is
        an argument the raise the TypeError
        """
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_initialized(self):
        """
        Test if the variable storage in model
        is actually an instance of FilStorage
        """
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        create an empty temporary file to
        save data
        """
        self.test_file = "test_file.json"

    def tearDown(self):
        """
        remove the temporary file of test
        after  test is done
        """
        if os.path.exists(self.test_file):

            os.remove(self.test_file)

    def test_all(self):
        """
        test all if they actually
        return a dictionary
        """
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """
        tests if the new create the
        new dictionary
        """
        my_obj = BaseModel()
        models.storage.new(my_obj)

        self.assertIn("BaseModel.{}".format(my_obj.id), models.storage.all())

    def test_new_with_args(self):
        """
        tests the new method with an argument
        if argument it will raise a TypeError
        """

        with self.assertRaises(TypeError):

            models.storage.new(BaseModel(), 1)

    def test_new_no_args(self):
        """
        tests the new method with no argument
        if argument it will raise an AttributError
        """

        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """
        tests to make sure data is
        surely save in file
        """
        obj1 = BaseModel()
        obj2 = BaseModel()

        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        new_storage = FileStorage()

        new_storage.reload()

        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj1.id)) is not None)
        self.assertTrue(new_storage.all().get("BaseModel.{}".format(obj2.id)) is not None)

    def test_save(self):
        """
        tests to make sure data is
        surely save in file
        """
        my_obj1 = BaseModel()
        models.storage.new(my_obj1)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_emp_file(self):
        """
        tests if file is empty during
        the loading file then
        raise a TypeError
        """

        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


if __name__ == "__main__":
    unittest.main()
