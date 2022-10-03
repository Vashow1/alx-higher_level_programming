"""Unittests for the base class"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Contains methods to the tests"""

    def test_basic_setup(self):
        """This fn checks whether the class is set up correct"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(13, 5)
        """
        Test if it gives it an id value equal to 1 since it is first
        If the optional values are set correctly
        And finally if the width and height values are correctly set
        """
        self.assertAlmostEqual(r1.id, r2.id - 1)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 2)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        """
        Test if the id increments and increments correctly and also if
        the other values are set up correctly
        """
        self.assertAlmostEqual(r3.id, 12)
        self.assertAlmostEqual(r3.width, 10)
        self.assertAlmostEqual(r3.height, 2)
        self.assertAlmostEqual(r3.x, 0)
        self.assertAlmostEqual(r3.y, 0)

        """
        Check whether the setters work proper
        """
        r3.width = 44
        r3.height = 55
        r3.x = 4
        r3.y = 8
        self.assertAlmostEqual(r3.width, 44)
        self.assertAlmostEqual(r3.height, 55)
        self.assertAlmostEqual(r3.x, 4)
        self.assertAlmostEqual(r3.y, 8)







