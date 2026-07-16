# Return a new array consisting of elements which are multiple of their own index
# in input array (length > 1).


def multiple_of_index(arr):
    return [value for index, value in enumerate(arr) if (value == 0 if index == 0 else value % index == 0)]


print(multiple_of_index([22, -6, 32, 82, 9, 25]))
print(multiple_of_index([68, -1, 1, -7, 10, 10]))
print(
    multiple_of_index(
        [-56, -85, 72, -26, -14, 76, -27, 72, 35, -21, -67, 87, 0, 21, 59, 27, -92, 68]
    )
)
