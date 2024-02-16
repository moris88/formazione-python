'''
Write a Python script to concatenate the following dictionaries to create a new one
'''


def concatenate_dictionaries(dictionaries):
    result = {}
    for dictionary in dictionaries:
        result.update(dictionary)
    return result

# Create three dictionaries 'dic1', 'dic2' and 'dic3' with key-value pairs.


dic1 = {'a': 1, 'b': 2}
dic2 = {'c': 3, 'd': 4}
dic3 = {'e': 5, 'f': 6}

print(concatenate_dictionaries([dic1, dic2, dic3]))


def alternative(*args, **kwargs):
    print(args)
    print(kwargs)


dic4 = {**dic1, **dic2, **dic3}
alternative(dic4)
