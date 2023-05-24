# Calcolatrice che esegua 3 calcoli in fila a scelta tra addizione, sottrazione e moltiplicazione che salvi ogni risultato in una lista 

class Calcolatrice:
    def __init__(self):
        self.lista = []

    def somma(self, num1, num2):
        return num1 + num2

    def moltiplicazione(self, num1, num2):
        return num1 * num2

    def differenza(self, num1, num2):
        return num1 - num2

    def totale(self):
        if not self.lista:
            print("Non ci sono risultati qui")
        else:
            somma = 0
            for risultato in self.lista:
                somma += risultato
            return somma

    def stampa_operazioni(self):
        if not self.lista:
            print("La lista è vuota")
        else:
            for risultato in self.lista:
                print(f"Il risultato dell'operazione è il seguente: {risultato}")


accensione = True
calcolatrice = Calcolatrice()

while accensione:
    print("Seleziona l'opzione desiderata")
    print("1. Somma")
    print("2. Moltiplicazione")
    print("3. Sottrazione")
    print("4. Esci")

    scelta = input("Inserisci la tua scelta: ")

    if scelta == "1":
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato = calcolatrice.somma(num1, num2)
        calcolatrice.lista.append(risultato)
        calcolatrice.stampa_operazioni()

    elif scelta == "2":
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato = calcolatrice.moltiplicazione(num1, num2)
        calcolatrice.lista.append(risultato)
        calcolatrice.stampa_operazioni()

    elif scelta == "3":
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato = calcolatrice.differenza(num1, num2)
        calcolatrice.lista.append(risultato)
        calcolatrice.stampa_operazioni()

    elif scelta == "4":
        accensione = False

    else:
        print("Scelta non valida")


