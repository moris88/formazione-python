'''
Scrivere una funzione ricorsiva che restituisce in output i numeri della successione di Fibonacci,
entro una soglia specifica impostata dall'utente.
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


soglia = int(input("Inserisci un numero: "))
for numero in range(soglia):
    print(fibonacci(numero))
