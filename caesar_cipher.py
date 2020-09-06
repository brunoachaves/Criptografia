#!/usr/bin/env python
from argparse import ArgumentParser


def convert(data_in, flag):
    ascii_code = [ord(char) for char in data_in]
    if not flag:
        print('starting the encrypt process')
        converted = [chr((code+3) % 127) for code in ascii_code]
    else:
        print('starting the decrypt process')
        converted = [chr((code-3) % 127) for code in ascii_code]
    data_out = "".join(converted)
    return converted, data_out


if __name__ == '__main__':
    ap = ArgumentParser()
    ap.add_argument('-i', '--input', type=str, help='input data')
    ap.add_argument('-d', '--decrypt', type=bool,
                    help='set True to decrypt the data.')
    args = ap.parse_args()

    try:
        _, output = convert(args.input, args.decrypt)
        print(f'original data: {args.input}')
        print(f'converted data: {output}')
    except Exception as e:
        print(e)
