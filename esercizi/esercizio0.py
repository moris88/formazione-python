test = input('Inserisci qualcosa: ')
if test.isdigit():
    test = int(test)
if test.lower() == "true" or test.lower() == "false":
    test = bool(test)
print(f'python => test is {type(test)}')