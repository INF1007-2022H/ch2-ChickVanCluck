#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    majmot = ''
    for c in mot:
        if 97<=ord(c)<=122
            majmot += chr(ord('c')-32)
        else 
            majmot += c
    return majmot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
