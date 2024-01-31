# write a python program to sort a list of dictionaries using lambda function

list_of_dictionaries = [
    {"name": "John", "age": 30, "color": "red"},
    {"name": "Mary", "age": 20, "color": "blue"},
    {"name": "Peter", "age": 10, "color": "green"},
    {"name": "John", "age": 30, "color": "black"},
]

list_of_dictionaries.sort(key=lambda x: x["color"])

print(f'La lista ordinata è: {list_of_dictionaries}')
