# Scrivi un programma che chiede all'utente di inserire una serie di parole separate da spazi.
# Il programma crea un insieme con le parole inserite e successivamente stampa l'insieme.

#possibilità inserimento parole 
parole = input("Inserisci le parole: ").split()     
print(parole)                                          

#creazione insieme vuoto
insieme =  set() 

#inserimento delle parole all'interno dell'insieme vuoto 
for parola in parole: 
    insieme.add(parola)

#mandare a schermo l'insieme 
print(insieme)   






#Scrivi un programma che prende due liste e crea un insieme contenente gli elementi presenti in entrambe le liste. 
#Stampa l'insieme risultante

lista1 = (input("Inserisci le parole nella lista: ")).split()
lista2 = (input("Inserisci le parole nella lista: ")).split()


insieme = set()


for parola in lista1: 
        insieme.add(parola)


for parola in lista2: 
    insieme.add(parola)
   
print(insieme)                            







#MODO ALTERNATIVO DI RISOLUZIONE 
lista1 = (input("Inserisci le parole nella lista: ")).split()
lista2 = (input("Inserisci le parole nella lista: ")).split()

insieme1 = set()
for parola in lista1: 
        insieme1.add(parola)

insieme2 = set()
for parola in lista2: 
        insieme2.add(parola)

print(lista1.union(lista2))
