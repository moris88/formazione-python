'''
Write a list comprehension in Python that takes a list of integers and returns a new list containing the square of the even numbers present in the starting list.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]

print(squared_even_numbers)

'''
From the previous python code, rewrite using a map and a lambda function?
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared_even_numbers = list(
    map(lambda x: x**2, (i for i in numbers if i % 2 == 0)))

print(squared_even_numbers)
