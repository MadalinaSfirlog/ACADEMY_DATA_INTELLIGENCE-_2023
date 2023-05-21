'''
Scrivere un programma python per la gestione di un registro vendite.
Il programma deve permettere di aggiungere le vendite di diversi prodotti e calcolare il totale delle vendite (per ogni prodotto)

Steps:  
1) Aggiungi una vendita di un prodotto (si richiede all'utente il nome del prodotto, la quantità ed il prezzo per unità)
2) Visualizzare il totale delle vendite per ogni prodotto presente nel registro 

'''

accensione = True
prodotti = {}

while accensione:
    print("Selezionare l'opzione desiderata")
    print("1. Registra una vendita")
    print("2. Visualizza il totale delle vendite")
    print("3. Esci")

    scelta = input("Inserisci la tua scelta: ")

    if scelta == '3':
        # richiesta uscita dal programma
        accensione = False

    elif scelta == '1':
        # richiesta registrazione di una vendita
        nome = input("Inserire il nome del prodotto: ").strip().lower()
        quantita = int(input("Inserire la quantità del prodotto: "))
        prezzo = float(input("Inserire il prezzo unitario del prodotto: "))

        # verifica positività prezzo e quantità
        if prezzo < 0 or quantita < 0:
            print("Errore, non puoi inserire una quantità o un prezzo negativo")
        else:
            # inserisco in dizionario prodotti con la quantità - valore e prezzo - valore
            prodotti[nome] = {"quantita": quantita, "prezzo": prezzo}
            
            print("\nVendita registrata correttamente")

    elif scelta == '2':

        # richiesta visualizzazione prodotti
        for nome, info in prodotti.items(): 
                                       
            quantita_prodotto = info["quantita"]                        
            prezzo_prodotto = info["prezzo"]
            totale_vendita = prezzo_prodotto * quantita_prodotto       
            
            #visualizzazione a schermo della vendita totale per prodotto
            print(f"Il totale vendita del prodotto {nome} è stata la seguente: {prezzo_prodotto} * {quantita_prodotto} = {totale_vendita}")
    
    else:
        # opzione inesistente
        print("Errore, l'opzione da te selezionata non esiste")

