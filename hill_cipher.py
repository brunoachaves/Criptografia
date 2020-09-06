#!/usr/bin/env python
import numpy as np

# Definindo tamanho do alfabeto, dados de entrada e chave de criptografia

data_in = 'SŢÕVŝØOƙóMŢÏEŰá'

alphabet_sz = 65536

enc_key = np.array([[1, 0, 0],
                    [1, 3, 1],
                    [1, 2, 0]])

# Convertendo o dado de entrada para uma matriz multiplicavel pela chave
print('\ninput encrypted data')
print(data_in)

# Decodificação
# 1 - Converta os dados de entrada para seus representantes numéricos
# 2 - Calcule o inverso da matriz usada como chave de criptografia
# 3 - Redimencione a lista de dados de entrada para virar uma matriz multiplicável pela inversa da chave
# 4 - Multiplique a matriz inversa pela matriz redimensionada com os dados de entrada
# fazendo o módulo pelo tamanho do alfabeto utilizado
# 5 - Redimensione a matriz resultante para uma lista
# 6 - Retorne os dados numérios para caracteres

# 1. Criando uma lista com os números correspondentes à cada dígito do dado de entrada
p = [ord(i) for i in data_in]
print('\nencrypted text values:')
print(p)

# 2. Calculando o inverso da chave de criptografia
inv = np.linalg.inv(enc_key)
print('\ninverse key:')
print(inv)

# 3. Redimensionando a lista de dados de entrada para virar uma matriz multiplicável pela inversa da chave
p_matrix = np.array(list(p)).reshape(5, 3).transpose()
print('\ndata values:')
print(p_matrix)

# 4. Multiplicando a matriz inversa pela matriz redimensionada com os dados de entrada
dec_matrix = np.dot(inv, p_matrix) % alphabet_sz
print('\ndecrypted matrix:')
print(dec_matrix)

# 5 - Redimensionando a matriz resultante para uma lista
dec_list = dec_matrix.transpose().flatten()
print('\nlist of decrypted values')
print(dec_list)

# 6 - Retornando os dados numérios para caracteres
converted = [chr(int(j)) for j in dec_list]
print(f'\noriginal data: {data_in}')
print(f'converted data: {"".join(converted)}')  # Convertendo a lista de chars para uma única string
