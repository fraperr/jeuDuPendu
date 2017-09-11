#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pickle # pour les fichiers en mode binaire
import donnees # liste des modules personnels
import random # permet de générer un nombre aléatoire
# import pdb # debug

# on vérifier que le joueur entre au moins un caractère.
nom =  donnees.saisirCaract("Veuillez saisir votre nom: ")

# Si le fichier existe on récupère le score dans la variable score
# sinon un crée un fichier de score vide
score = donnees.fichierExiste("scores")

# vérifier si le joueur existe, sinon le créer avec un score de 0
# et l'enregistrer dans le fichier
try:
	score[nom]
except KeyError:
	score[nom] = 0

# affichage du score
print("Votre score actuel: "  + str(score[nom]))
with open("scores", "wb") as fichier:
	monPickler = pickle.Pickler(fichier)
	monPickler.dump(score)

# on récupère la liste des mots
listeDesMots = donnees.dico()
nombreDeMots = len(donnees.dico()) # calcul du nombre de mots
choixDuMot = random.randrange(nombreDeMots) # on en choisit un au hasard
unMot = listeDesMots[choixDuMot]

# Affichichage du mot cachée sous forme '*' et creation d'un liste contenant
# la même chose
motCache = donnees.insereDesEtoiles(unMot)
motCacheL = list(motCache)

i = 0
# pdb.set_trace()
reponse = ''
while i < 8 and reponse.lower() != unMot:
	# Le joueur peut choisir une lettre
	choixLettre = ''
	while len(choixLettre) != 1:
		choixLettre = donnees.saisirCaract("Choisissez une lettre: ").lower()
		if len(choixLettre) > 1:
			print("Vous n'avez droit qu'à une seule lettre.")

	# On convertir la chaine de caractère mot en dictionaire.
	unMotL = list(unMot)
	listeDesPositions = donnees.trouveToutesLesPositions(unMotL, choixLettre)

	# On remplce les étoiles par la lettre trouvée.
	for position in listeDesPositions:
		del motCacheL[position]
		motCacheL.insert(position, choixLettre)

	print(donnees.listEnChaine(motCacheL))
	i += 1

	ouiNon = ''
	while ouiNon != "o".lower() and ouiNon != "n".lower():
		ouiNon = input("Voulez-vous donner la solution: ")

	if ouiNon == "o":
		reponse = input("Introduisez votre mot: ")

if reponse.lower() == unMot:
	print("Bravo vous avez gagné!")
	points = 8 - i
	score[nom] += points
else:
	print("Désolé, vous avez perdu!")

print("Votre score est de : ", score[nom])

