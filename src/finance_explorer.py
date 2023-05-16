import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt




def button_click():
    show_kontostand_plot()
    

def show_kontostand_plot():
    # Spalten, die behalten werden sollen
    columns_to_keep = ["Buchungstag", "Saldo nach Buchung"]

    # Lade die CSV-Datei mit Pandas und behalte nur die angegebenen Spalten
    data = pd.read_csv("data/Transactions_2023-03.csv", delimiter=";", usecols=columns_to_keep)

    # Konvertiere das Datumsformat in einen geeigneten Datentyp
    data["Buchungstag"] = pd.to_datetime(data["Buchungstag"], format="%d.%m.%Y")

    # Konvertiere den Kontostand in den korrekten Datentyp und ändere das Dezimaltrennzeichen
    data["Saldo nach Buchung"] = data["Saldo nach Buchung"].str.replace(",", ".").astype(float)

    # Erstelle den Plot des Kontostands
    plt.plot(data["Buchungstag"], data["Saldo nach Buchung"])
    plt.xlabel("Buchungstag")
    plt.ylabel("Saldo nach Buchung")
    plt.title("Kontostand über Zeit")
    plt.xticks(rotation=45)
    plt.show()





root = tk.Tk()
root.title("Finance Explorer")  # Titel des Fensters

label = tk.Label(root, text="Willkommen zum Finance Explorer")
label.pack()  # Platziere das Label im Hauptfenster

button = tk.Button(root, text="Klick mich", command=button_click)  # command=button_click weist dem Button die Funktion button_click() als Aktion zu
button.pack()  # Platziere den Button im Hauptfenster

root.mainloop()