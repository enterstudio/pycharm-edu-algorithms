from test_helper import run_common_tests, failed, passed
from fibonacci_number import fibonacci_number


def fibonacci_number_reference(n):
    assert 0 <= n <= 40
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


if __name__ == '__main__':
    run_common_tests()

    all_tests_passed = True
    for x in range(41):
        if fibonacci_number(x) != fibonacci_number_reference(x):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(x))
            break

    if all_tests_passed:
        passed()
