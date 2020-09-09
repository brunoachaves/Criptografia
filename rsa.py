#!/usr/bin/env python
from functools import reduce
import numpy as np
import os
import time


# Organizando o print de um número grande, convertendo-o para hexadecimal
def print_large_number(large_number):
    string = "{:02x}".format(large_number)
    for j in range(len(string)):
        if j % 64 == 0 and j > 0:
            print()
        print(string[j], end="")
    print()


# Gerando dois números primos cujo o produto tenha 4096 bits
def get_primes(min_value, max_value):
    while True:
        prime_1 = int(os.popen("openssl prime -generate -bits 2048").read()[:-1])
        prime_2 = int(os.popen("openssl prime -generate -bits 2048").read()[:-1])
        prime_1_2 = prime_1 * prime_2
        if min_value < prime_1_2 < max_value:
            break
    return prime_1, prime_2, prime_1_2


# Método para auxiliar no cálculo do inverso multiplicativo modular
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# Calculando o inverso multiplicativo modular
def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('[Erro] inverso multiplicativo modular não existe!')
    else:
        return x % m


if __name__ == '__main__':
    # Recebendo o texto de entrada
    data_in = input('Digite o texto de entrada:\n')
    begin = time.time()
    bit_length = 4096

    # Gerar os números primos adequados
    n_min = 1 << (bit_length - 1)
    n_max = (1 << bit_length) - 1
    p, q, n = get_primes(n_min, n_max)
    print(f'\nTamanho da chave = {len(bin(n)[2:])} bits')
    print('\nPrimeiro número primo:')
    print_large_number(p)
    print('\nSegundo número primo:')
    print_large_number(q)

    # Calculando a função totiente phi(N)
    phi = (p - 1) * (q - 1)
    # Calculando o 'e'
    e = 65635
    while np.gcd(e, phi) > 1:
        e += 2
    # Calculando o módulo inverso multiplicativo
    d = mod_inv(e, phi)

    print('\nDado original:')
    print(data_in)

    # Encriptando o texto
    nbytes = min(len(data_in), bit_length - 1)
    data_int = reduce(lambda x, y: (x << 8) + y, map(ord, data_in[:bit_length]))
    encrypted_int = pow(data_int, e, n)
    encrypted_list = [(encrypted_int >> j) & 0xff for j in reversed(range(0, bit_length, 8))]
    print('\nDado encriptado:')
    print_large_number(encrypted_int)

    # Decriptando o texto
    decrypted_list = reduce(lambda x, y: (x << 8) + y, encrypted_list[:bit_length + 2])
    decrypted_int = pow(decrypted_list, d, n)
    decrypted = "".join([chr((decrypted_int >> j) & 0xff) for j in reversed(range(0, bit_length, 8))])
    print('\nDado decriptado:')
    print(decrypted)

    # Tempo de execução
    print(f'\nTempo de execução: {round(time.time() - begin, 2)}')