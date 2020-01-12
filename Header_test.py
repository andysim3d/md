import unittest
from Header import Header
class TestStringMethods(unittest.TestCase):

    def test_header_render(self):
        h1 = Header("test", 1)
        self.assertEqual(h1.render(), "<h1> test </h1>")
        h1 = Header("hello", 2)
        self.assertEqual(h1.render(), "<h2> hello </h2>")
        h1 = Header("hello world", 3)
        self.assertEqual(h1.render(), "<h3> hello world </h3>")

if __name__ == '__main__':
    unittest.main()

