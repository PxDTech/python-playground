"""Module for summing positive numbers in a list."""


def positive_sum(arr):
    """Return sum of positive numbers in arr."""
    return sum(x for x in arr if x > 0)


if __name__ == "__main__":
    example = [1, -4, 7, 12]
    print(positive_sum(example))
