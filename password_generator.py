"""
GERADOR DE SENHA
SIMPLES E RÁPIDO
"""

import random

minusculo = 'abcdefghijklmnopqrstuvwxyz'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!@#$%&*/\?'

use_for = minusculo + maiusculo + numeros + simbolos
tamanho_da_senha = 15
# OBS: Para te maior ou menor número de caracter altere o valor acima (15), para a quantidade desejada.

password = "".join(random.sample(use_for, tamanho_da_senha))

print('Sua senha gerada é: ' + password)
