# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a 
    soma dos números que não são múltiplos de 13 entre X e Y, incluindo 
    ambos.

    Entrada
    O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente 
    em ordem crescente.

    Saída
    Imprima a soma de todos os valores não divisíveis por 13 entre os 
    dois valores lidos na entrada, inclusive ambos se for o caso.
"""


X = int(input())
Y = int(input())

soma = 0

if X < Y:
    i = X
    while i <= Y:
        if not i % 13 == 0:
            soma += i
        i += 1

else:
    i = Y
    while i <= X:
        if not i % 13 == 0:
            soma += i
        i += 1

print(soma)
exit(0)