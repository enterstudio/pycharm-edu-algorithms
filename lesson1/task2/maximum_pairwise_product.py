#python3 (this comment is needed by the autograding system at Coursera and edX)

def max_pairwise_product_naive(A):
    assert len(A) >= 2
    assert all(0 <= x and x <= 2 * 10**5 for x in A)

    product = 0

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            product = max(product, A[i] * A[j])

    return product

def max_pairwise_product(A):
    assert len(A) >= 2
    assert all(0 <= x and x <= 2 * 10**5 for x in A)
    type here

# TODO: when your solution is ready, uncomment the following three lines and submit to Coursera/edX
# if __name__ == '__main__':
#     n = int(input())
#     A = [int(x) for x in input().split()]
#     assert len(A) == n
#     print(max_pairwise_product(A))


