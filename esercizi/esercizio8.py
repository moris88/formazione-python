'''
Rewrite the python code to simplify the following functions into lambda function:
numbers = [1,2,3,4,5,6,7,8,9]

def myFunc(x):
    return x+x
    
result = filter(myFunc, numbers)
print(list(result))

Rewrite the python code to simplify the following functions into lambda function:
ages = [5,12,17,18,24,32]

def myFunc(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc, ages)
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = map(lambda x: x+x, numbers)
print(list(result))

ages = [5, 12, 17, 18, 24, 32]

adults = filter(lambda x: x >= 18, ages)
print(list(adults))
