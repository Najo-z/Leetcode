#!/usr/bin/env python3

import sys
import os
import requests
import json


def main():
    if len(sys.argv) == 1:
        print('Provide problem number as argument.')
        return
    problem = int(sys.argv[1])
    path = f'{problem}.py'
    if os.path.exists(path):
        print(f'Problem number file already exists: {path}.')
        return
    with open('problems.txt', 'r') as f:
        lines = [v.replace('\n', '') for v in f.readlines()]
    id = ''
    for split in [line.split(';') for line in lines]:
        if int(split[0]) == problem:
            id = split[1]
            break
    with open(path, 'w') as f:
        f.write(f'# Problem name: {id}\n\n')


if __name__ == '__main__':
    main()
