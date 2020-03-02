import unittest
import json

from PeNumbers import PeNumbers

class testPeNumbers(unittest.TestCase):

    def setUp(self):
        self.PeNumbers = PeNumbers()

    def test_divisible_by_3(self):
        expected_result = "P"
        number = 3
        
        res = self.PeNumbers.return_p_e(number)
        error = "Divisible by 3 failed. Got "+str(res)+" Expected: "+expected_result
        self.assertEquals(res, expected_result, error)
        
    def test_divisible_by_5(self):
        expected_result = "E"
        number = 20

        res = self.PeNumbers.return_p_e(number)
        error = "Divisible by 5 failed. Got "+str(res)+" Expected: "+expected_result
        self.assertEquals(res, expected_result, error)
        
    def test_divisible_by_3_and_5(self):
        expected_result = "PE"
        number = 15

        res = self.PeNumbers.return_p_e(number)
        error = "Divisible by 3 and 5 failed. Got "+str(res)+" Expected: "+str(expected_result)
        self.assertEquals(res, expected_result, error)

    def test_any_other_number(self):
        number = 334
        expected_result = number 

        res = self.PeNumbers.return_p_e(number)
        error = "Non divisible by 3 or 5 failed. Got "+str(res)+" Expected: "+str(expected_result)
        self.assertEquals(res, expected_result, error)

    def test_bad_input(self):        
        number = "ThisIsInvalid"
        self.assertRaises(TypeError, self.PeNumbers.return_p_e(number), "Exception not raised")
        
        
if __name__ == "__main__":
    unittest.main()
