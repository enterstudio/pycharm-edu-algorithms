# python3 (this comment is needed by the grading system at Coursera and edX)


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10**5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10**5 for x in numbers)
    type here


# TODO: when your solution is ready, uncomment the following three lines and submit to Coursera/edX
# if __name__ == '__main__':
#     n = int(input())
#     input_numbers = [int(x) for x in input().split()]
#     assert len(input_numbers) == n
#     print(max_pairwise_product(input_numbers))
