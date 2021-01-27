#-*- conding=utf-8 -*-
from time import time 
import matplotlib.pyplot as plt



def suite_geometrique():
	U0=1
	U1=2
	S=U0+U1
	return S

def suite_arithmetique():
	U0=1
	U1=2
	U2=4
	S1=U0+U1+U2
	return S1 

def term_some_geo():
	U0=1
	U1=2
	U2=4
	U3=8
	S2=U0+U1+U2+U3
	return S2


clock=time()
suite_geometrique()
clock = time() - clock

clock1=time()
suite_arithmetique()
clock1= time() - clock1

clock2=time()
term_some_geo()
clock2= time() - clock2

print("value clock=",clock , "value clock1=", clock1)

plt.plot([clock, clock1, clock2])
plt.grid()
plt.ylabel('Fréquence des caractères')
plt.xlabel('Les caractères')
plt.title('DECRYPTER LES MESSAGES CRYPTES BY LANDRIS18')
plt.show()
