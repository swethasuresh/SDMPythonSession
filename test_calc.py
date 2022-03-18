import unittest
import calculator


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 5), 6)
        self.assertEqual(calculator.sub(1, 5), -4)
        self.assertEqual(calculator.mul(2, 4), 8)
        self.assertEqual(calculator.div(1, 5), 3)
