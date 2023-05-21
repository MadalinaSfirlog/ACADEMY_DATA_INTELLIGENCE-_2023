#Scrivi un programma che chiede all'utente di inserire una serie di numeri.
#Il programma stampa i numeri fino a quando l'utente non inserisce il numero 0. In tal caso, il programma esce dal ciclo utilizzando l'istruzione break.

lista_numeri = input("Inserisci i numeri: ").split()

for numero in lista_numeri: 
        if numero == "0": 
            break
        else: 
            print(numero)    




#Creare un menu dove si da la possibilità all'utente di inserire una serie di numeri 
#Se il numero è diverso da zero il menu deve mandare a schermo i numeri inseriti 
#Se il numero è uguale a zero il ciclo deve interrompersi e l'accensione deve spegnersi

accensione = True
while accensione: 
    lista_numeri = input("Inserisci i numeri: ").split()               
            
    for numero in lista_numeri:            
     if numero != "0":  
        print(numero)
     else:
        break
        accensione=False




