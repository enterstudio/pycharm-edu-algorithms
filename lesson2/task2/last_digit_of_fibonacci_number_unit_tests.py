import unittest
from last_digit_of_fibonacci_number import last_digit_of_fibonacci_number

def fibonacci_number_naive(n):
    assert 0 <= n and n <= 20

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


class TestLastDigitOfFibonacciNumber(unittest.TestCase):
    def test_small(self):
        for n in range(20):
            self.assertEqual(fibonacci_number_naive(n) % 10, last_digit_of_fibonacci_number(n))


    def test_large(self):
        for (n, last_digit) in [(100, 5), (139, 1), (91239, 6)]:
            self.assertEqual(last_digit_of_fibonacci_number(n), last_digit)


if __name__ == '__main__':
    unittest.main()
