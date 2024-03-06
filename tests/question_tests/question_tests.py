#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_random_number
from src.question_b.question_b import get_sum_of_evens
from src.question_c.question_c import get_tax_assessed, get_assessment_value
from src.question_d.question_d import is_prime

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    # this one is commented because it can either fail or pass and both are acceptable
    #def test_get_random_number(self):
    #    self.assertEqual(get_random_number(), 5)

    # get sum of evens
    def test_get_sum_of_evens_1(self):
        self.assertEqual(get_sum_of_evens(11), 30)
    def test_get_sum_of_evens_2(self):
        self.assertEqual(get_sum_of_evens(10), 30)
    def test_get_sum_of_evens_3(self):
        self.assertEqual(get_sum_of_evens(8), 20)

    # get assessment value
    def test_get_assessment_value_1(self):
        self.assertEqual(get_assessment_value(10000), 6000)
    def test_get_assessment_value_2(self):
        self.assertEqual(get_assessment_value(20000), 12000)
    # get tax assessed
    def test_get_tax_assessed_1(self):
        self.assertEqual(get_tax_assessed(6000), 43.20)
    def test_get_tax_assessed_2(self):
        self.assertEqual(get_tax_assessed(10000), 72)

    # is prime?
    def test_is_prime_1(self):
        self.assertEqual(is_prime(4), False)
    def test_is_prime_2(self):
        self.assertEqual(is_prime(5), True)
    def test_is_prime_3(self):
        self.assertEqual(is_prime(11), True)