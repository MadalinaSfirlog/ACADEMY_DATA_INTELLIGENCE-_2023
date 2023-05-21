#Scrivi un programma che stampa i numeri da 1 a 10, ma salta il numero 5 utilizzando l'istruzione continue.

for numero in range(1,11): 
    if numero == 5: 
        continue 
    else: 
        print(numero)






#Scrivi un programma che chiede all'utente di indovinare un numero compreso tra 1 e 10. 
#Il programma continua a chiedere all'utente di indovinare finché non indovina correttamente.

#definire un numero 
numero = 7 

accensione = True

while accensione: 
    scelta = int(input("Scegli un numero compreso tra 1 a 10 "))

    if scelta > 10 or scelta < 1: 
        print("Scelta non permessa. Riprova")
    else: 
        if scelta != numero:
            print("Non hai indovinato. Riprova")
        else:
            print("Hai indovinato! Il numero è", numero)
            access_flag = True







#Stesso esercizio con AND 
numero = 7 

accensione = True

while accensione: 
    scelta = int(input("Scegli un numero compreso tra 1 a 10 "))

    if scelta < 10 and scelta > 1: 
        if scelta != numero:
            print("Non hai indovinato. Riprova")
        else:
            print("Hai indovinato! Il numero è", numero)
            access_flag = True







#Stesso esercizio con modulo RANDOM 

import random 

lista = []

for numero in range(1,11): 
    lista.append(numero)

numero_random = random.choice(lista)

accensione = True
while accensione:

    scelta = int(input("Scegli un numero compreso tra 1 a 10 "))

    if scelta > 10 or scelta < 1: 
        print("Scelta non permessa. Riprova")
    else: 
        if scelta != numero_random:
            print("Non hai indovinato. Riprova")
        else:
            print("Hai indovinato! Il numero è", numero_random)
            accensione = False





