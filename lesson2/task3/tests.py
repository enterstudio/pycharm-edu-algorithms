import math
from test_helper import run_common_tests, failed, passed
from gcd import gcd

if __name__ == '__main__':
    run_common_tests()

    all_tests_passed = True
    for (a, b) in [(2, 3), (10**8, 10**5 - 1), (10**8, 10**9)]:
        if gcd(a, b) != math.gcd(a, b):
            all_tests_passed = False
            failed("Wrong answer for a={}, b={}".format(a, b))
            break

    if all_tests_passed:
        passed()


