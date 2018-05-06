# python3 (this comment is needed by the grading system at Coursera and edX)
import sys


def maximum_loot_value(capacity, weights, values):
    value = 0.
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
