# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:19:05 2019

@author: Pedro Augusto
"""

import textwrap

def align_text(text, length):
    # define um comprimento máximo para cada linha
    broken_text = ''
    for parag in text:
        if parag == '\n':
            broken_text = broken_text + '\n\n'
        else:
            broken_text = broken_text + '\n'.join(textwrap.wrap(parag, length, break_long_words=False))
    return broken_text

def items_len(l):
    return sum([ len(x) for x in l] )

def align_line(text, width):
    # justifica o texto
    left, right, w = '', text, width
    items = right.split()

    # adiciona um espaço entre cada palara, menos a última
    for i in range(len(items) - 1):
        items[i] += ' '

    left_count = w - items_len(items)
    while left_count > 0 and len(items) > 1:
        for i in range(len(items) - 1):
            items[i] += ' '
            left_count -= 1
            if left_count < 1:  
                break

    res = left + ''.join(items)
    
    return res

if __name__ == "__main__":
    length = 40 #No máximo 40
    with open("input.txt", 'r') as f:
        file = f.readlines()
        
    text = align_text(file, length).splitlines()
    new_text = []
    
    for l in text:
        new_text.append(align_line(l, length))

    print("\nTexto Formatado:\n\n{0}".format('\n'.join(new_text)))