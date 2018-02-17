import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello worldd'
        self.assertEqual(s.split(), ['hello', 'worldd'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_equal(self):
        a=3
        b=5
        self.assertEqual(a,b)


if __name__ == '__main__':
    unittest.main()
