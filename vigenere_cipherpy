#!/usr/bin/env python

def convert(data_in, key_in, action_in):
    # Criando a lista do alfabeto minusculo de 'a' à 'z' e definindo seu tamanho
    alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    alphabet_sz = len(alphabet)

    # Criando uma lista com os números correspondentes à cada letra do texto e da chave
    p = [alphabet.index(i) for i in data_in]
    k = [alphabet.index(i) for i in key_in]

    # Definindo o tamanho do texto (n) e da chave (m)
    n = len(p)
    m = len(k)

    if action_in:  # Criptografar
        converted = [alphabet[(p[i]+k[i % m]) % alphabet_sz] for i in range(n)]
    else:  # Decriptografar
        converted = [alphabet[(p[i]-k[i % m]) % alphabet_sz] for i in range(n)]

    return "".join(converted)  # Juntando os elementos da lista para formar uma mesma string


if __name__ == '__main__':
    # Listas com as palavras que podem ser apresentadas no enunciado
    action_msg = ['decriptografar', 'criptografar']
    result_msg = ['decriptografado', 'criptografado']

    # Recebimento das variáveis do processo
    action = '1' in input('\nVocê deseja criptografar <1> ou decriptografar uma mensagem <2>?\n')
    text = input(f'\nDigite o texto que deseja {action_msg[action]}?\n').upper()
    key = input(f'\nDigite a chave que deseja usar:\n').upper()

    # Apreentação do resultado
    print(f'\nTexto {result_msg[action]}:')
    print(convert(text, key, action))
