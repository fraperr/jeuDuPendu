#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle # pour les fichiers en mode binaire
import donnees # liste des modules personnels
import fonction
import random # permet de générer un nombre aléatoire
# import pdb # debug

# on vérifier que le joueur entre au moins un caractère.
nom =  fonction.saisirCaract("Veuillez saisir votre nom: ")

# Si le fichier existe on récupère le score dans la variable score
score = fonction.fichierExiste("scores")

# vérifier si le joueur existe, sinon le créer avec un score de 0
try:
	score[nom]
except KeyError:
	score[nom] = 0

# affichage du score
print("Votre score actuel: "  + str(score[nom]))

# on récupère la liste des mots
listeDesMots = donnees.dico()
nombreDeMots = len(donnees.dico()) # calcul du nombre de mots
choixDuMot = random.randrange(nombreDeMots) # on en choisit un au hasard
unMot = listeDesMots[choixDuMot]

# Affichichage du mot cachée sous forme '*' et creation d'un liste contenant
# la même chose
motCache = fonction.insereDesEtoiles(unMot)
motCacheL = list(motCache)

i = 0 # initialisation du compteur
# pdb.set_trace()
reponse = '' # initialisation de reponse
nbreDeTours = donnees.nombreChances()
while i < nbreDeTours and reponse.lower() != unMot: # on a droit a 8 chances
	# Le joueur peut choisir une lettre
	choixLettre = ''
	while len(choixLettre) != 1: # Une seule lettre peut-être saisie
		choixLettre = fonction.saisirCaract("Choisissez une lettre: ").lower()
		if len(choixLettre) > 1:
			print("Vous n'avez droit qu'à une seule lettre.")

	# On convertir la chaine de caractère mot en dictionaire.
	unMotL = list(unMot)
	# Indice de toutes les occurences possibles
	listeDesPositions = fonction.trouveToutesLesPositions(unMotL, choixLettre)

	# On remplce les étoiles par la lettre trouvée.
	for position in listeDesPositions:
		del motCacheL[position]
		motCacheL.insert(position, choixLettre)

	# Affichage du résultat
	print(fonction.listEnChaine(motCacheL))
	i += 1 # Tour suivant

	# L'utilisateur a la possiblité de trouver le mot
	ouiNon = ''
	while ouiNon != "o".lower() and ouiNon != "n".lower():
		ouiNon = input("Voulez-vous donner la solution: ")

	if ouiNon == "o":
		reponse = input("Introduisez votre mot: ")
# En cas de réussite on affiche un message et on ajuste les points
if reponse.lower() == unMot:
	print("Bravo vous avez gagné!")
	points = 8 - i
	score[nom] += points
	fonction.enregistre(score, "scores")
else:
	print("Désolé, vous avez perdu!")

# Affichage du score final
print("Votre score est de : ", score[nom])

