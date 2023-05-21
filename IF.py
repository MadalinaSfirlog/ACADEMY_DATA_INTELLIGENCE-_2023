#Scrivi un programma che chiede all'utente di inserire un numero. 
#Se il numero è positivo, stampa "Il numero è positivo". 
#Se il numero è negativo, stampa "Il numero è negativo". 
#Se il numero è zero, stampa "Il numero è zero".


numero = int(input("Inserisci un numero: "))

if numero > 0: 
    print("Il numero è positivo")
elif numero < 0: 
    print("Il numero è negativo")
elif numero == 0: 
    print("Il numero è zero")




#Scrivi un programma che chiede all'utente di inserire un numero intero positivo. 
# Se il numero è pari, stampa "Il numero è pari". 
# Se il numero è dispari, stampa "Il numero è dispari".

numero = int(input("Inserisci un numero: "))

if numero < 0: 
    print("Il numero non è positivo, riprova!")

elif numero % 2 == 0: 
    print("Il numero è pari")


elif numero % 2 != 0: 
    print("Il numero è dispari")

else: 
    print("Inserire un numero intero positivo")

