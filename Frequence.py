# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
file_name=input("Enter your file here: ")
file=open(file_name)
dico={}
liste=[]
for ligne in file:
	letters=list(ligne)
	for letter in letters:
		if letter not in liste:
			dico[letter]=1
	for letter in letters:
		if letter not in liste:
			liste.append(letter)
		else:
			dico[letter]= int(dico[letter])+1
print("Les frequences des caracteres sont ####  ", dico)
plt.plot(dico.keys(),dico.values())
plt.grid()
plt.ylabel('Fréquence des caractères')
plt.xlabel('Les caractères')
plt.title('DECRYPTER LES MESSAGES CRYPTES BY JUNO JAH')
plt.show()
