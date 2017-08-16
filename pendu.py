#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle # pour les fichiers en mode binaire
import donnees
import random

# on vérifier que le joueur entre au moins un caractère.
messageNom = "Veuillez saisir votre nom: "
nom =  donnees.saisirCaract(messageNom)
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

# on récupère la liste des mots
listeDesMots = donnees.dico()
nombreDeMots = len(donnees.dico()) # calcul du nombre de mots
choixDuMot = random.randrange(nombreDeMots) # on en choisit un au hasard
print(nombreDeMots)
unMot = listeDesMots[choixDuMot]

motCache = ''
for lettre in unMot:
    motCache += '*'
motCacheL = list(motCache)
print(motCache)

i = 0
while i < 8:
    choixLettre = input("Choisissez une lettre: ")
    unMotL = list(unMot)
    try:
        position =  unMotL.index(choixLettre)
    except ValueError:
        print("Cette lettre n'est pas dans le mot")
    else:
        del motCacheL[position]
        motCacheL.insert(position, choixLettre)
    motCache = ''
    for lettre in  motCacheL:
        motCache += lettre
    i += 1

print(motCache)
