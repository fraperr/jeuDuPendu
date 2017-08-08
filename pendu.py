#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle

nom = input("Veuillez saisir votre nom: ")

try:
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scoreRecupere = monDepickler.load()
except FileNotFoundError:
   fichier = open('scores', 'w')
   fichier.close()

