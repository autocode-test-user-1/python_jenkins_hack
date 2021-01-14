import unittest

from main import add


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2, add(1, 1))


if __name__ == '__main__':
    unittest.main()
