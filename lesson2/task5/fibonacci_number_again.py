# python3 (this comment is needed by the autograding system at Coursera and edX)


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 5

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 5
    type here


# TODO: when your solution is ready, uncomment the following three lines and submit to Coursera/edX
# if __name__ == '__main__':
#     input_n, input_m = map(int, input().split())
#     print(fibonacci_number_again(input_n, input_m))