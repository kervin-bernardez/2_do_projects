import unittest
from ceasar_shift_cipher import encode


class TestEncode(unittest.TestCase):
    def test_basic(self):
        testcase = "abcd"
        expected = "cdef"
        shift = -2
        self.assertEqual(encode(testcase, shift), expected)

    def test_ignore(self):
        testcase = "Ωñæÿ$"
        expected = "Ωñæÿ$"
        shift = -4
        self.assertEqual(encode(testcase, shift), expected)

    def test_null(self):
        testcase = ""
        expected = ""
        shift = -1
        self.assertEqual(encode(testcase, shift), expected)

    def test_zero_shift(self):
        testcase = "abcd"
        expected = "abcd"
        shift = 0
        self.assertEqual(encode(testcase, shift), expected)

    def test_integer_shift(self):
        testcase = "abcd"
        expected = "efgh"
        shift = -4
        self.assertEqual(encode(testcase, shift), expected)

    def test_floor_float_shift(self):
        testcase = "abcd"
        expected = "efgh"
        shift = -4.1
        self.assertEqual(encode(testcase, shift), expected)

    def test_roof_float_shift(self):
        testcase = "abcd"
        expected = "efgh"
        shift = -4.9
        self.assertEqual(encode(testcase, shift), expected)

    def test_big_shift(self):
        testcase = "Hello World"
        expected = "Dahhk Sknhz"
        shift = -100
        self.assertEqual(encode(testcase, shift), expected)

    def test_bigger_shift(self):
        testcase = "Hello World"
        expected = "Tqxxa Iadxp"
        shift = -1000
        self.assertEqual(encode(testcase, shift), expected)


if __name__ == '__main__':
    unittest.main()
