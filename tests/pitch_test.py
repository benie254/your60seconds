import unittest
from app.models import Pitch


class PitchTest(unittest.TestCase):
    """
    test behavior of Pitch class
    """

    def setUp(self):
        """
        runs before every test
        """

        self.new_pitch = Pitch('A pitch like none other', 'Pitch content here--one or multiple lines', 'general')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))
