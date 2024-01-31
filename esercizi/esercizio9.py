# scrivi una list comprehension che prende una lista di numeri interi e restituisce una nuova lista contenente il quadrato dei numeri pari presenti nella lista di partenza

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]

print(squared_even_numbers)

# usando una map e la lambda function?

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# squared_even_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
squared_even_numbers = list(map(lambda x: x**2, (i for i in numbers if i % 2 == 0)))

print(squared_even_numbers)