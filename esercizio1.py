def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = 25
converted_fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {converted_fahrenheit} degrees Fahrenheit.")

fahrenheit = 77
converted_celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_celsius} degrees Celsius.")

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
converted_celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} degrees Fahrenheit is equal to {converted_celsius} degrees Celsius.")
