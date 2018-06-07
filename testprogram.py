import day2.testing.calculator as cal

import unittest

class TestUM( unittest.TestCase) :

    def setUp(self):
        print("Setup is called")

    def test_number_3_5(self):
        self.assertEqual(cal.multiply(3,5),15,"Multipliction not working")

    def test_number_a_3(self):
        self.assertEqual(cal.multiply('a',3),'aaa',"Multipliction on string not working")

    def tearDown(self):
        print("Teardown is called")

if __name__ == '__main__' :
    unittest.main()
