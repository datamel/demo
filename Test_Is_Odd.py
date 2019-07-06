import unittest
import Another as An


class TestOdd(unittest.TestCase):
    
    def test_if_odd_number_returns_true(self):
        self.assertEqual(An.oddy(3),True , "Odd Number")

    def test_if_even_number_returns_false(self):
        self.assertEqual(An.oddy((2)), False, "Even Number")
    def test_if_exceptions_thrown_on_not_number_given(self):
        with self.assertRaises(ValueError): An.oddy("j")
if __name__ == '__main__':
    unittest.main()
