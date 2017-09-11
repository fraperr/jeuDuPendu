#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle # pour les fichiers en mode binaire

def insereDesEtoiles(mot):
    motCache = ''
    for lettre in mot:
        motCache += '*'
    return motCache

def dico():
    mots = ["bâteau", "chat", "pendule", "soleil", "lune", "malade", "citron",
            "boisson", "prière", "vinaigre", "vitesse", "oignon", "bière",
            "bâton", "bientôt", "terre", "vide", "raisin", "écran", "bible",
            "tasse", "gravier", "peste", "électron", "lune", "truite", "mouche",
            "rève", "nage", "ivre", "glace", "chemin", "religion", "effet",
            "fièvre", "malade", "crise", "angoisse", "ver", "savon", "douche",
            "propre", "saleté", "médecin", "calcul", "vide"]
    return mots

def nombreChances():
    return 8

def saisirCaract(message):
    estVide = True
    while estVide:
        saisie = input(message)
        if saisie.isalpha():
            estVide = False
        else:
            print("Vous ne pouvez saisir que des lettres.")
    return saisie

# vérifier si le fichier des scores existe, si ce n'est pas le cas
# la fonction renvoie une variable dictionnaire contenant les scores des joueurs
def fichierExiste(monFichier):
    try:
        with open(monFichier, 'rb') as fichier:
            monDepickler = pickle.Unpickler(fichier)
            score = monDepickler.load()

    except FileNotFoundError:
        score = {}

    return score

def trouveToutesLesPositions(motL, lettre):
    i = 0
    positionL = []
    while i < len(motL):
        # On vérifie si la lettre choisit est dans le mot.
        try:
            position =  motL.index(lettre, i)
        except ValueError:
            i = len(motL)
        # Dans ce cas on remplace l'étoile par la lettre et on affiche
        # la nouvelle chaine ainsi formée.
        else:
            positionL.append(position)
            i = position + 1
    return positionL

def listEnChaine(liste):
    chaine = ''
    for elem in liste:
        chaine += elem
    return chaine

def enregistre(monFichier):
	with open(monFichier, 'wb') as fichier:
		monDepickler = pickle.Pickler(fichier)
		score = monDepickler.dump()
