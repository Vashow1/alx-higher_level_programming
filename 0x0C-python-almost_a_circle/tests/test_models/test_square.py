"""Unittests for the base class"""
import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    """Contains methods to the tests"""

    def test_basic_setup(self):
        """This fn checks whether the class is set up correct"""
        s1 = Square(10)
        s2 = Square(13)
        """
        Test if it gives it an id value equal to 1 since it is first
        If the optional values are set correctly
        And finally if the width and height values are correctly set
        """
        self.assertAlmostEqual(s1.id, s2.id - 1)
        self.assertAlmostEqual(s1.size, 10)
        self.assertAlmostEqual(s1.x, 0)
        self.assertAlmostEqual(s1.y, 0)

        s3 = Square(10, 1, 1, 12)
        """
        Test if the id increments and increments correctly and also if
        the other values are set up correctly
        """
        self.assertAlmostEqual(s3.id, 12)
        self.assertAlmostEqual(s3.size, 10)
        self.assertAlmostEqual(s3.x, 1)
        self.assertAlmostEqual(s3.y, 1)

        """
        Check whether the setters work proper
        """
        s3.size = 44
        s3.x = 4
        s3.y = 8
        self.assertAlmostEqual(s3.size, 44)
        self.assertAlmostEqual(s3.x, 4)
        self.assertAlmostEqual(s3.y, 8)







