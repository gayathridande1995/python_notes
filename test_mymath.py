import mymath
import unittest

class TestAdd(unittest.TestCase) :
    def test_add_integer(self):
        """ Test that the addition of integers return correct value"""
        result=mymath.add(3,5)
        self.assertEqual(result,9)

    def test_add_strings(self):
        """ Test that the addition of strings return correct value"""
        result=mymath.add("abc","def")
        self.assertEqual(result,"abcdef")

    if __name__ =='__main__':
        unittest.main()
