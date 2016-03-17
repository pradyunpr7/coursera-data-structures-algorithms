# Uses python3


def get_fibonacci_last_digit(n):
    """Last digit of N-th element of Fibonacci sequence.

    Computing the last digit of F[i] is easy: it is just the last digit of
    the sum of the last digits of F[i−1] and F[i−2]. The matrix representation
    for the Fibonacci numbers is used here:

    | 1 1 | n   | F[n+1] F[n]   |
    |     |   = |               |
    | 1 0 |     | F[n]   F[n-1] |

    Samples:
    >>> get_fibonacci_last_digit(3)
    2
    >>> get_fibonacci_last_digit(327305)
    5
    """
    m = [[1, 1],
         [1, 0]]

    for _ in range(2, n + 1):
        m00 = m[0][0] % 10
        m10 = m[1][0] % 10
        m = [
            [m00 + m[0][1] % 10, m00],
            [m10 + m[1][1] % 10, m10]
        ]

    return m[0][1]


if __name__ == "__main__":
    n = int(input())
    print(get_fibonacci_last_digit(n))
