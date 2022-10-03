"""Unittests for the base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Contains methods to the tests"""

    def test_basic_setup(self):
        """This fn checks whether the class is set up correct"""
        b1 = Base()
        """Test if it gives it an id value equal to 1 since it is first"""
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base(23)
        """Test if it gives it a unique id value since it is supplied with one"""
        self.assertAlmostEqual(b2.id, 23)
        b3 = Base()
        """Test if the id increments and increments correctly"""
        self.assertAlmostEqual(b3.id, 2)
