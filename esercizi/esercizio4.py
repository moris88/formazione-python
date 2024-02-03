'''
Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
'''

def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

print(count_strings(['abc', 'xyz', 'aba', '1221']))
