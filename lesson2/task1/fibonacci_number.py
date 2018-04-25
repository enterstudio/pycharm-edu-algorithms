#python3 (this comment is needed by the autograding system at Coursera and edX)

def fibonacci_number_naive(n):
    assert 0 <= n and n <= 40

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n and n <= 40
    write your code here


# TODO: when your solution is ready, uncomment the following three lines and submit to Coursera/edX
# if __name__ == '__main__':
#     n = int(input())
#     print(fibonacci_number(n))

