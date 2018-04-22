from test_helper import run_common_tests, failed, passed, get_answer_placeholders
from fibonacci_number import fibonacci_number

def fibonacci_number_reference(n):
    assert 0 <= n and n <= 40
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current

if __name__ == '__main__':
    run_common_tests()

    all_tests_passed = True
    for n in range(41):
        if fibonacci_number(n) != fibonacci_number_reference(n):
            all_tests_passed = False
            failed("Wrong answer for n={}".format(n))
            break

    if all_tests_passed:
        passed()


