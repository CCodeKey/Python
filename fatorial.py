from math import factorial
from collections import Counter

def calculo(palavra):
    n = len(palavra)
    contador = Counter(palavra)
    repeticoes = 1
    for letra, freq in contador.items():
        repeticoes *= factorial(freq)
    anagramas = factorial(n)
    return anagramas, repeticoes

palavra = input("Digite uma palavra > ")
anagramas, repeticoes = calculo(palavra)
print(f"A palavra '{palavra}' possui :")
print( f"{anagramas} anagramas;")
print(f"{repeticoes} repetições.")
print()
print()

