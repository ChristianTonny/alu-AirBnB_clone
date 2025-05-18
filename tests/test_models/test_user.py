#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User
from models.base_model import BaseModel # Important for type checks and inheritance tests


class TestUserInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def test_user_instantiation(self):
        """Test that User class can be instantiated."""
        user = User()
        self.assertIsInstance(user, User)

    def test_user_inherits_from_base_model(self):
        """Test that User inherits from BaseModel."""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_id_is_public_str(self):
        """Test that id is a public string attribute (inherited)."""
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        """Test that created_at is a public datetime attribute (inherited)."""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test that updated_at is a public datetime attribute (inherited)."""
        self.assertEqual(datetime, type(User().updated_at))

    def test_user_attributes_are_present_and_correct_type_and_default(self):
        """Test that User specific attributes are present, have correct type and default value."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(type(user.email), str)
        self.assertEqual(user.email, "")

        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(type(user.password), str)
        self.assertEqual(user.password, "")

        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(user.first_name, "")

        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(type(user.last_name), str)
        self.assertEqual(user.last_name, "")

    def test_instantiation_with_kwargs(self):
        """Test instantiation with kwargs."""
        dt = datetime.now()
        dt_iso = dt.isoformat()
        u = User(id="123", created_at=dt_iso, updated_at=dt_iso, email="test@example.com", first_name="Test")
        self.assertEqual(u.id, "123")
        self.assertEqual(u.created_at, dt)
        self.assertEqual(u.updated_at, dt)
        self.assertEqual(u.email, "test@example.com")
        self.assertEqual(u.first_name, "Test")

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation with None kwargs (should be handled by BaseModel)."""
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittests for testing the save method of the User class."""

    @classmethod
    def setUpClass(cls):
        """Set up for save tests. Rename file.json if it exists."""
        try:
            os.rename("file.json", "tmp_file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down for save tests. Remove file.json and rename tmp_file.json back."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp_file.json", "file.json")
        except FileNotFoundError:
            pass

    def test_one_save(self):
        """Test that save method updates updated_at."""
        user = User()
        sleep(0.05)  # Ensure time difference
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_save_updates_file(self):
        """Test that save method writes to file.json."""
        user = User()
        user.save()
        uid = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(uid, f.read())


class TestUserToDict(unittest.TestCase):
    """Unittests for testing the to_dict method of the User class."""

    def test_to_dict_type(self):
        """Test that to_dict returns a dictionary."""
        self.assertEqual(dict, type(User().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict contains all expected keys."""
        user = User()
        user_dict = user.to_dict()
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test that datetime attributes in to_dict are strings."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict["created_at"]))
        self.assertEqual(str, type(user_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict for a User instance."""
        dt = datetime.now()
        u = User(id="123", created_at=dt, updated_at=dt)
        u.email = "test@example.com"
        u.first_name = "Betty"
        
        # Note: BaseModel's to_dict converts created_at and updated_at to isoformat strings
        # So, for comparison, we also need to use isoformat for these fields.
        # Other attributes are taken directly.
        
        expected_dict = {
            'id': '123',
            '__class__': 'User',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
            'email': 'test@example.com',
            'password': '', # Default if not set
            'first_name': 'Betty',
            'last_name': ''  # Default if not set
        }
        # Update the user's actual timestamps to match dt for a predictable dict
        u.created_at = dt
        u.updated_at = dt
        
        self.assertDictEqual(u.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main() 