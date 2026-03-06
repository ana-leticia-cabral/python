# Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

letra = input('Digite uma letra: ')

print(type(letra))
print(letra.isalnum())
print(letra.isalpha())
print(letra.isnumeric())
