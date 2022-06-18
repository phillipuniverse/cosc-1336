import unittest
from decimal import Decimal

from project3.main import calculate_fee


class FeesTests(unittest.TestCase):

    def test_given_sample(self):
        self.assertEqual(Decimal("11.0"), calculate_fee(10))

    def test_fewer_than_20(self):
        self.assertEqual(Decimal("10"), calculate_fee(0))
        self.assertEqual(Decimal("10.4"), calculate_fee(4))
        self.assertEqual(Decimal("11.9"), calculate_fee(19))

    def test_20_to_39(self):
        self.assertEqual(Decimal("11.6"), calculate_fee(20))
        self.assertEqual(Decimal("12.16"), calculate_fee(27))
        self.assertEqual(Decimal("13.12"), calculate_fee(39))

    def test_40_to_59(self):
        self.assertEqual(Decimal("12.4"), calculate_fee(40))
        self.assertEqual(Decimal("12.94"), calculate_fee(49))
        self.assertEqual(Decimal("13.54"), calculate_fee(59))

    def test_60_or_more(self):
        self.assertEqual(Decimal("12.4"), calculate_fee(60))
