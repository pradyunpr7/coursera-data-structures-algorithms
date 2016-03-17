# Uses python3


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    """Least Common Multiple of a and b.

    The least common multiple of two positive integers a and b is the least
    positive integer m that is divisible by both a and b.

    Samples:
    >>> lcm(6, 8)
    24
    >>> lcm(28851538, 1183019)
    1933053046
    """
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
