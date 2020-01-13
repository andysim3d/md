import unittest
from Element import Text
from Header import Header, LineSperator, Quote
class TestStringMethods(unittest.TestCase):

    def test_header_render(self):

        h1 = Header("test", 1)
        self.assertEqual(h1.render(), "<h1> test </h1>")
        h1 = Header("hello", 2)
        self.assertEqual(h1.render(), "<h2> hello </h2>")
        h1 = Header(("hello world"), 3)
        self.assertEqual(h1.render(), "<h3> hello world </h3>")

    def test_sep_render(self):
        h1 = LineSperator()
        self.assertEqual(h1.render(), "<hr class='line_sep'/>")
    
    def test_quote(self):
        quote = Quote("hello world")
        self.assertEqual(quote.render(), "<blockquote> hello world </blockquote>")
        quote_wrap = Quote(quote)
        self.assertEqual(quote_wrap.render(), "<blockquote> <blockquote> hello world </blockquote> </blockquote>")


if __name__ == '__main__':
    unittest.main()

