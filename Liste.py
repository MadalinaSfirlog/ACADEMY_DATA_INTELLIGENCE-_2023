#Scrivi un programma che chiede all'utente di inserire una serie di numeri separati da virgole.
#Il programma dovrebbe creare una lista con i numeri inseriti e stamparla
#E poi sommarli 

lista = list()                                 
numeri = input("Inserisci il numero: ")            #Inserisci il numero: 1,2,3,4

lista = numeri.split(",")
print(lista)                                        #['1', '2', '3', '4']                     

nuova_lista = list()

for elemento in lista: 
    x = int(elemento)                 
    nuova_lista.append(x)

print(nuova_lista)                                  #[1, 2, 3, 4]               

somma = 0

for i in nuova_lista:
    somma += i

print(somma)                                         #10




#Creare un menu con 3 possibilità; entrare, visualizzare la lista, uscire. 
#Se l'utente sceglie uscire l'applicazione il menù si chiude. 
#Se l'utente sceglie di entrare deve avere la possibilità di aggiungere i numeri inseriti uno alla volta alla lista e mandarla a schermo
#Se l'utente sceglie di visualizzare la lista, la lista deve essere mandata a schermo
#Creare opzione inesistente 

lista = []                                 



accensione = True 

while accensione: 
    print("\nBenvenuto. Selezionare l'opzione desiderata")
    print("1. Entra per inserire i numeri")
    print("2. Visualizza tutta la lista")
    print("0. Esci")
    
    scelta = input("Inserisci la tua scelta: ")

    if scelta == '0':
        #richiesta uscita dal programma
        accensione = False
    
    
    elif scelta == '1':
        #aggiungere i numeri alla lista 
       numeri = int(input("Inserisci il numero: ")) 
       lista.append (numeri)
       print(lista)
           
    elif scelta == '2':
        #visualizzare la lista  
            print(f"Questi sono gli elementi: {lista}")

    else:
        #opzione inesistente
        print("Errore, l'opzione da te selezionata non esiste")





