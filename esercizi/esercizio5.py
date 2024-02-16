'''
Write a Python a function to find the maximum sum sub-sequence in a list. Return the maximum value.
'''


def max_subsequence_sum(sequence):
    max_sum = 0
    current_sum = 0

    for number in sequence:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_subsequence_sum([1, 2, 4, 3, 5, 4, 6, 9, 2, -10]))
