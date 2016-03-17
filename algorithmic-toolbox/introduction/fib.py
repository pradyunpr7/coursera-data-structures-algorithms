# Uses python3


def calc_fib(n):
    """N-th element of Fibonacci sequence.

    The Fibonacci numbers are defined as follows:
    F[0] = 0, F[1] = 1, and F[i] = F[i−1] + F[i−2] for i ≥ 2.

    Samples:
    >>> calc_fib(3)
    2
    >>> calc_fib(10)
    55
    """
    if n <= 1:
        return n

    a, b = (0, 1)
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
