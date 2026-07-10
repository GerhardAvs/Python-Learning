numero = int(input('Dame el numero para sacar factorial: '))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(numero))
    