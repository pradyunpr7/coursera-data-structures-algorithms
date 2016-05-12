# Uses python3
import random
import sys


def partition2(a, left, right):
    """2-way partitioning.

    Reorder the array so that all elements with values less than the pivot come
    before the pivot, while all elements with values greater than the pivot come
    after it (equal values can go either way).
    After this partitioning, the pivot is in its final position.

    Samples:
    >>> a = [2, 3, 9, 2, 2]
    >>> partition2(a, 0, 4)
    2
    >>> # Explanation: 2 is an index of pivot element after 2-way partitioning
    >>> # is done.
    >>> a
    [2, 2, 2, 3, 9]
    """
    pivot = a[left]
    j = left
    for i in range(left + 1, right + 1):
        if a[i] <= pivot:
            j += 1
            a[i], a[j] = a[j], a[i]

    pivot, a[j] = a[j], pivot
    return j


def partition3(a, left, right):
    """3-way partitioning.

    This method is useful when array contains lot of duplicate values which is
    very frequent in real world. Idea is to divide array in three parts rather
    than two. First part contains all numbers which are less than the pivot,
    second part contains number equal to the pivot and last part contains
    numbers which are greater than pivot.

    Samples:
    >>> a = [2, 1, 2, 3, 2, 2, 2, 3, 1, 2, 1, 2, 3, 3, 2, 2, 1, 3, 1]
    >>> partition3(a, 0, 18)
    (5, 13)
    >>> # Explanation: 5 and 13 is the index range where the pivot elements are
    >>> # located after 3-way partitioning is done.
    >>> a
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
    """
    pivot = a[left]
    i = left
    lt = left
    gt = right
    while i <= gt:
        if a[i] < pivot:
            a[i], a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def randomized_quick_sort(a, left, right):
    if left >= right:
        return

    random_pivot = random.randint(left, right)
    a[left], a[random_pivot] = a[random_pivot], a[left]

    # use partition3
    mid1, mid2 = partition3(a, left, right)
    randomized_quick_sort(a, left, mid1 - 1)
    randomized_quick_sort(a, mid2 + 1, right)


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=" ")
