# Semplificare le seguenti funzioni in lambda function

numbers = [1,2,3,4,5,6,7,8,9]

def myFunc1(x):
    return x+x
    
result1 = filter(myFunc1, numbers)
print(list(result1))

result2 = map(lambda x: x+x, numbers)
print(list(result2))

ages = [5,12,17,18,24,32]

def myFunc2(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myFunc2, ages)

for x in adults:
    print(x)
    
adults = filter(lambda x: x >= 18, ages)
print(list(adults))