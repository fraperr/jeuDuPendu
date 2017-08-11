#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle # pour les fichiers en mode binaire

nom = input("Veuillez saisir votre nom: ")

# vérifier si le fichier des scores existe, si ce n'est pas le cas
# créer un dictionaire gérant le score
try:
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        score = monDepickler.load()

except FileNotFoundError:
    score = {}

# vérifier si le joueur existe, sinon le créer avec un score de 0
# et l'enregistrer dans le fichier
try:
    score[nom]
except KeyError:
    score[nom] = 0
    with open("scores", "wb") as fichier:
        monPickler = pickle.Pickler(fichier)
        monPickler.dump(score)

# récupérer le fichier du score et l'affecter au dictionaire score.
with open("scores", "rb") as fichier:
    monDepickler = pickle.Unpickler(fichier)
    score = monDepickler.load()

print(score)
