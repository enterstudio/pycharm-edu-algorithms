from test_helper import run_common_tests, failed, passed
from last_digit_of_fibonacci_number import last_digit_of_fibonacci_number

def fibonacci_number_last_digit_reference(n):
    assert 0 <= n and n <= 10**6
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

if __name__ == '__main__':
    run_common_tests()

    all_tests_passed = True
    for n in [2, 3, 239, 240, 1000, 9999, 10**6]:
        if last_digit_of_fibonacci_number(n) != fibonacci_number_last_digit_reference(n):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(n))
            break

    if all_tests_passed:
        passed()


