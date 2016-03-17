# Uses python3


def gcd(a, b):
    """Greatest Common Divisor of a and b.

    The greatest common divisor GCD(a, b) of two non-negative integers
    a and b (which are not both equal to 0) is the greatest integer d that
    divides both a and b.

    (a, b) on each iteration:
    28851538 1183019
    1183019  459082
    459082   264855
    264855   194227
    194227   70628
    70628    52971
    52971    17657
    17657    0

    Samples:
    >>> gcd(18, 35)
    1
    >>> gcd(28851538, 1183019)
    17657
    """
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
