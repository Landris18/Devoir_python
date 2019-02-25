# COMPTER LES MOTS DANS UN FICHIER
"""
   D'abord on récupère le document choisi par les utilisateurs.
   Alors les utilisateurs doivent saisir le nom du document qu'ils veulent compter.
"""

# Ici les utilisateurs saisissent le nom du document
Doc = input("Entrer le nom du document qu'on va compter: ")

#On récupère ce document.
a = open(Doc)

# On va changer en liste par ligne les contenus et on va enlever les éspaces pour que notre programme ne les tiennent pas en compte comme mot.
c = 0
for b in a:
	b = b.split(" ")
	c = c + len(b)

# Enfin, on va afficher le nombre de mot dans le fichier que l'utilisateur saisisse.
print(c)
