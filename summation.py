# Write a program that finds the summation of every number from 1 to num (both inclusive). The number will always be a positive integer greater than 0.

# def summation(num):
#     total = 0
#     for n in range(num + 1):
#         total = total + n
#     return total


def summation(num):
    return sum(range(1, num + 1))


print(summation(2))
print(summation(8))
