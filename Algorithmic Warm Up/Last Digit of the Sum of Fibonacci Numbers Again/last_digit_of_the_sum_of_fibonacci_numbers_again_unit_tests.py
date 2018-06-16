import unittest
from last_digit_of_the_sum_of_fibonacci_numbers_again import last_digit_of_the_sum_of_fibonacci_numbers_again


class TestLastDigitOfTheSumOfFibonacciNumbersAgain(unittest.TestCase):
    def test(self):
        for (from_index, to_index, last_digit) in [(3, 7, 1), (10, 10, 55), type here]:
            self.assertEqual(last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index), last_digit)


if __name__ == '__main__':
    unittest.main()
