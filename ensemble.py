import matplotlib.pyplot as plt
a=input("Entrer ici le doc: ");
b= open(a,"r")
liste = []
dico = {}

def compterMots(b):
	for x in b:
		x = x.split(" ")
		for i in x:
			dico[i] = 1

	for x in b:
		x = x.split(' ')
		for i in x:
			if i not in liste:
				liste.append(i)
			else:
				y = int(dico[i]) +1
				dico[i] = y
	print(f"La fréquence de tout les mots: {dico}")
compterMots(b)

