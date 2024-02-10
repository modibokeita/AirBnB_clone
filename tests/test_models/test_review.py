#!/usr/bin/python3
import os
import models
from models.base_model import BaseModel
from models.review import Review
import unittest
"""
Review test Module
"""


class TestReview(unittest.TestCase):
    """
    set up all possible cases
    for Review model
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

    def test_review_attr(self):
        """
        test the review attribute when
        the new instance of user was
        created
        """
        test_review = Review()
        self.assertEqual(test_review.place_id, "")
        self.assertEqual(test_review.user_id, "")
        self.assertEqual(test_review.text, "")

    def test_state_inherit(self):
        """
        test if the new instance of Riview was created
        and the instance of review inherit from
        Base model class
        """
        test_inherit = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_str(self):
        """
        test if the review attributes return
        string representation
        """
        test_review = Review()
        test_review.place_id = "psd12"
        test_review.user_id = "ksd12"
        test_review.text = "something"

        review_str = str(test_review)
        self.assertIn("Review", review_str)
        self.assertIn("psd12", review_str)
        self.assertIn("ksd12", review_str)
        self.assertIn("something", review_str)

    def test_review_to_dict(self):
        """
        test if the new instance of review
        was created it return a dictoinary
        """
        test_review = Review()
        test_review.place_id = "psd12"
        test_review.user_id = "ksd12"
        test_review.text = "something"
        test_review.save()

        review_dict = test_review.to_dict()
        self.assertEqual(review_dict['place_id'], "psd12")
        self.assertEqual(review_dict['user_id'], "ksd12")
        self.assertEqual(review_dict['text'], "something")


if __name__ == "__main__":
    unittest.main()
