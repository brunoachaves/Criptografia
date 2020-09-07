#!/usr/bin/env python
import numpy as np
from math import log10
import os


def print_hex_list(int_list):
    """Print ciphertext in hex"""
    for index, elem in enumerate(int_list):
        print("{:02x}".format(elem), end="")
    print()


def print_large_integer(number):
    """Print long primes in a formatted way"""
    string = "{:02x}".format(number)
    for j in range(len(string)):
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


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def mod_inv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


if __name__ == '__main__':
    data_in = input('Digite o texto de entrada:\n')
    bit_length = 4096

    n_min = 1 << (bit_length - 1)
    n_max = (1 << bit_length) - 1
    p, q, n = get_primes(n_min, n_max)
    print(f'\nTamanho da chave = {len(bin(n)[2:])} bits')
    print('\nPrimeiro número primo:')
    print_large_integer(p)
    print('\nSegundo número primo:')
    print_large_integer(q)

    phi = (p - 1) * (q - 1)
    e = 65635
    while np.gcd(e, phi) > 1:
        e += 2
    d = mod_inv(e, phi)

    # print('\nFunção totiente:')
    # print_large_integer(phi)
    # print('\ne:')
    # print(e)
    # print(f'\nd:')
    # print_large_integer(d)

    encrypted = pow(ord(data_in), e, n)
    decrypted = pow(encrypted, d, n)
    print('\nDado original:')
    print(data_in)
    print('\nDado encriptado:')
    print_large_integer(encrypted)
    print('\nDado decriptado:')
    print(chr(decrypted))
