# python3 (this comment is needed by the autograding system at Coursera and edX)


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18
    type here


# TODO: when your solution is ready, uncomment the following three lines and submit to Coursera/edX
# if __name__ == '__main__':
#     input_n = int(input())
#     print(last_digit_of_the_sum_of_fibonacci_numbers_naive(input_n))
