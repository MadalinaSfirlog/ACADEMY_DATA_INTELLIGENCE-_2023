#Scrivi un programma che rappresenta un dizionario contenente i nomi dei mesi come chiavi e il numero di giorni come valori. 

dizionario = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
} 

# Crea un menu con due possibilità di scelta: inserire nome del mese, uscire. 
# Se l'utente scegliere di uscire, l'applicazione si chiude. 
# Se l'utente sceglie di inserire il nome di un mese, il programma stampa il numero di giorni corrispondente utilizzando il dizionario.

accensione = True 

while accensione: 
    print("\nBenvenuto. Selezionare l'opzione desiderata")
    print("1. Inserire nome mese")
    print("0. Esci")
    
    #possibilità scelta utente
    scelta = input("Inserisci la tua scelta: ")

    if scelta == '0':
        #richiesta uscita dal programma
        accensione = False
    
    
    elif scelta == '1':
        ##possibilità inserimento mese 
        mese = input("Inserisci il mese: ").lower()
        
        #assegnazione del numero del giorno corrispondente al mese nel dizionario 
        if mese in dizionario: 
           numero_giorno = dizionario[mese]     
        print(f'Il numero dei giorni in {mese} è {numero_giorno}')
    
    else: 
        print("Scelta inserita errata")
    






#Scrivi un programma che chiede all'utente di inserire una frase. 
#Il programma conta quante volte ogni lettera appare nella frase e stampa il risultato utilizzando un dizionario
dizionario = {}



frase = input("Inserisci una frase; ").lower()  
print(frase)                                               

#eliminazione dei simboli
frase_corretta = "" 

for carattere in frase: 
    if carattere in ".,?! ": 
    
       pass                                   
            
    else: 
        frase_corretta += carattere         
print(frase_corretta)

#contare quante volte ogni lettera appare nella frase ed aggiungerlo al dizionario
for lettera in frase_corretta: 
    if lettera not in dizionario.keys(): 
        dizionario[lettera] = 1
    else: 
        dizionario[lettera] += 1



#Stampa il risultato utilizzando un dizionario.
print(dizionario)
