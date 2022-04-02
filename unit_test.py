import unittest

def sum_numbers(x, y):
    return x+y

class SimpleTest(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_numbers(3,4), 7)

# or use pytest

def test_sum_numbers():
    assert sum_numbers(3,4) == 7

test_sum_numbers()