#Create a menu that allows to create an user object with first name, last name, password and money. 
#Add a login and registration. If logged in, it allows to change data or delete his account.


class Utenti:
    def __init__(self, Nome, Cognome, Password, Soldi ):
        self.Nome = Nome
        self.Cognome = Cognome
        self.Password = Password
        self.Soldi = Soldi


Lista_utenti = []

def crea_utente():
       Nome = str(input("Inserisci il tuo nome: "))
       
       Cognome = str(input("Inserisci il tuo cognome: "))   
    
       Password = input("Inserisci la tua password: ")

       Soldi= float(input("Inserisci la quantità di denaro: "))
       

       Utente= Utenti(Nome, Cognome, Password, Soldi )
       Lista_utenti.append(Utente)

       print(f"L'utente è stato registrato correttamente con i seguenti dati: Nome -> {Nome}, Cognome -> {Cognome}, Password -> {Password}, Soldi -> {Soldi}")
       


def login():

    if len(Lista_utenti) == 0:
        print("Prego registrarsi per poter effetuare il login, grazie!")
        crea_utente()

    else:        
       Nome= str(input("Inserisci il tuo nome: "))
       Password= input("Inserisci la tua password: ")

       for Utente in Lista_utenti:
        if Utente.Nome == Nome and Utente.Password == Password:
            print("Credenziali inserite correttamente, login effettuato!")
            return menu_loggato(Utente)

        else:
            print("Credenziali invalide, riprovare.")

def cambia_password(Utente):
    nuova_password = input("Inserire la nuova password: ")
    Utente.Password = nuova_password
    print("La Password è stata cambiata con successo!")
    print(f"La nuova Password è la seguente: {nuova_password}")
          
def cambia_quantita_soldi(Utente):
    nuovi_soldi= float(input("Inserire la nuova quantità di denaro: "))
    Utente.Soldi = nuovi_soldi
    print("La quantità di denaro è stata cambiata con successo!")
    print(f"La nuova quantità di denaro è la seguente: {nuovi_soldi}")

def cancella_account(Utente):
     
    print("1. Conferma la rimozione dell'account")
    print("2. Ritorna al menù principale")
    
    scelta = input("Inserisci la tua scelta: ")

    if scelta == "1": 
        Lista_utenti.remove(Utente)
        print("Account eliminato con successo!")
    else:
        print("Ritorno al menù principale effettuato")
        menu_loggato(Utente)
    
def menu_loggato(Utente):
    accensione = True
    
    while accensione:
        print("Benvenuto!")
        print("Scegliere l'opzione desiderata")
        print("1. Cambiare la password")
        print("2. Cambiare i soldi")
        print("3. Cancellare l'account")
        print("0. Esci")
  
        
        scelta = input("Inserisci la tua scelta: ")

        if scelta == "1":
            cambia_password(Utente)
        elif scelta == "2":
            cambia_quantita_soldi(Utente)
        elif scelta == "3":
            cancella_account(Utente)
            accensione = False
            break
        elif scelta == "0":
            accensione = False
            print("Uscita dal menù di login avvenuta con successo!")
        
        
        else:
            print("L'opzione da te inserita non è corretta, riprovare")

def Menu_principale():
    accensione = True
    
    while accensione:
        
        print("Benvenuto nel menu. \nScegliere l'opzione desiderata")
        print("1. Creare Account")
        print("2. Login")
        print("0. Esci")
        
        scelta = input("Inserisci la tua scelta: ")
        print()

        if scelta == "0": 
                #conferma l'uscita
                accensione = False 
                print("Sei uscito dal menu, arrivederci!")
    
        if scelta == "1":
            crea_utente()
        
        elif scelta == "2": 

            Utente = login()
            
            if Utente:
                menu_loggato(Utente)
        
        else: 
            print("L'opzione da te selezionata è errata, riprovare")     


# Iniziare il programma
Menu_principale()