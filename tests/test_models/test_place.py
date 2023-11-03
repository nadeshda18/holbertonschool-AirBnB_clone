#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.my_place = Place()
        self.my_place.city_id = "SF"
        self.my_place.user_id = "user1"
        self.my_place.name = "My Place"
        self.my_place.description = "A nice place"
        self.my_place.number_rooms = 3
        self.my_place.number_bathrooms = 2
        self.my_place.max_guest = 4
        self.my_place.price_by_night = 100
        self.my_place.latitude = 37.7749
        self.my_place.longitude = -122.4194
        self.my_place.amenity_ids = ["amenity1", "amenity2"]

    def test_id(self):
        """Test id"""
        self.assertEqual(type(self.my_place.id), str)

    def test_attributes(self):
        """Test the attributes of Place"""
        self.assertEqual(self.my_place.city_id, "SF")
        self.assertEqual(self.my_place.user_id, "user1")
        self.assertEqual(self.my_place.name, "My Place")
        self.assertEqual(self.my_place.description, "A nice place")
        self.assertEqual(self.my_place.number_rooms, 3)
        self.assertEqual(self.my_place.number_bathrooms, 2)
        self.assertEqual(self.my_place.max_guest, 4)
        self.assertEqual(self.my_place.price_by_night, 100)
        self.assertEqual(self.my_place.latitude, 37.7749)
        self.assertEqual(self.my_place.longitude, -122.4194)
        self.assertEqual(self.my_place.amenity_ids, ["amenity1", "amenity2"])


def test_attributes_default(self):
    """ Test attributes default for Place """
    self.assertEqual(self.place1.city_id, "")
    self.assertEqual(self.place1.user_id, "")
    self.assertEqual(self.place1.name, "")
    self.assertEqual(self.place1.description, "")
    self.assertEqual(self.place1.number_rooms, 0)
    self.assertEqual(self.place1.number_bathrooms, 0)
    self.assertEqual(self.place1.max_guest, 0)
    self.assertEqual(self.place1.price_by_night, 0)
    self.assertEqual(self.place1.latitude, 0.0)
    self.assertEqual(self.place1.longitude, 0.0)
    self.assertEqual(self.place1.amenity_ids, [])  # Change to an empty list


def test_inheritance(self):
    """ Test inheritance from BaseModel """
    self.assertTrue(issubclass(Place, BaseModel))


def test_to_dict(self):
    """ Test to_dict for Place """
    expected = {
        "id": self.place2.id,
        "__class__": type(self.place2).__name__,
        "city_id": "123456",
        "user_id": "7890",
        "name": "Beautiful Beach House",
        "description": "A lovely place by the beach",
        "number_rooms": 3,
        "number_bathrooms": 2,
        "max_guest": 6,
        "price_by_night": 150,
        "latitude": 37.7749,
        "longitude": -122.4194,
        "amenity_ids": ["wifi", "pool"],
        "created_at": self.place2.created_at.isoformat(),
        "updated_at": self.place2.updated_at.isoformat()
    }
    self.assertDictEqual(self.place2.to_dict(), expected)


def test_str(self):
    """ Test str for the Place """
    expected = "[Place] ({}) {}".format(self.place2.id, self.place2.__dict__)
    self.assertEqual(str(self.place2), expected)


def test_save(self):
    """ Test save for the Place """
    created_at = self.place1.created_at
    updated_at = self.place1.updated_at
    self.place1.save()
    self.assertEqual(created_at, self.place1.created_at)
    self.assertNotEqual(updated_at, self.place1.updated_at)


if __name__ == '__main__':
    unittest.main()
