import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import os


# Pfad zum "Data"-Ordner
data_folder = "data"

# Liste der Dateien im "Data"-Ordner filtern, um nur CSV-Dateien zu erhalten
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

def button_click():
    show_kontostand_plot()

def show_kontostand_plot():
    # Spalten, die behalten werden sollen
    columns_to_keep = ["Buchungstag", "Saldo nach Buchung"]

   # Ausgewählter Dateiname aus der Combobox abrufen
    selected_file = dropdown.get()

    # Pfad zur ausgewählten CSV-Datei erstellen
    file_path = os.path.join("data", selected_file)

    # Lade die CSV-Datei mit Pandas und behalte nur die angegebenen Spalten
    data = pd.read_csv(file_path, delimiter=";", usecols=columns_to_keep)

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


def show_cost_pie_chart():
    # Spalten, die behalten werden sollen
    columns_to_keep = ["Verwendungszweck", "Betrag"]

    # Lade die CSV-Datei mit Pandas und behalte nur die angegebenen Spalten
    data = pd.read_csv("data/Transactions_2023-03.csv", delimiter=";", usecols=columns_to_keep)

    # Konvertiere den Datentyp der Spalte "Betrag" in float
    data["Betrag"] = data["Betrag"].str.replace(",", ".").astype(float)

    # Filtere nach Kosten (negative Beträge)
    kosten_data = data[data["Betrag"] < 0]

    # Benutzerdefinierte Funktion zur Gruppierung der Verwendungszwecke
    def group_verwendungszweck(verwendungszweck):
        if "Wintering" in verwendungszweck:
            return "Bäcker"
        elif "Fehren" in verwendungszweck:
            return "Bäcker"
        elif "Puls" in verwendungszweck:
            return "Bäcker"
        elif "Apotheke" in verwendungszweck:
            return "Apotheke"
        elif "Miete" in verwendungszweck:
            return "Miete"
        elif "Mobilfunk" in verwendungszweck:
            return "Mobilfunk"
        else:
            return "Sonstiges"

    # Füge eine neue Spalte hinzu, die die gruppierten Verwendungszwecke enthält
    kosten_data["Gruppierte Verwendungszwecke"] = kosten_data["Verwendungszweck"].apply(group_verwendungszweck)

    # Gruppiere nach den gruppierten Verwendungszwecken und berechne die Gesamtkosten pro Kategorie
    grouped_data = kosten_data.groupby("Gruppierte Verwendungszwecke").sum()

    # Verwende die absoluten Werte der negativen Beträge
    grouped_data["Betrag"] = grouped_data["Betrag"].abs()

    # Berechne die Gesamtkosten
    gesamtausgaben = grouped_data["Betrag"].sum()

    # Erstelle das Pie Chart
    labels = grouped_data.index + " " + grouped_data["Betrag"].map("{:.2f}".format) + "€" 
    plt.pie(grouped_data["Betrag"], labels=labels)
    plt.title("Gesamtausgaben: " + "{:.2f}".format(gesamtausgaben) + "€")
    plt.axis('equal')
    plt.show()
  
def show_kontostand_all_plot():
    # Spalten, die behalten werden sollen
    columns_to_keep = ["Buchungstag", "Saldo nach Buchung"]

    # Erstelle leere Listen für x- und y-Werte
    x_values = []
    y_values = []

    # Durchlaufe alle CSV-Dateien
    for file in csv_files:
        file_path = os.path.join(data_folder, file)

        # Lade die CSV-Datei mit Pandas und behalte nur die angegebenen Spalten
        data = pd.read_csv(file_path, delimiter=";", usecols=columns_to_keep)

        # Konvertiere das Datumsformat in einen geeigneten Datentyp
        data["Buchungstag"] = pd.to_datetime(data["Buchungstag"], format="%d.%m.%Y")

        # Konvertiere den Kontostand in den korrekten Datentyp und ändere das Dezimaltrennzeichen
        data["Saldo nach Buchung"] = data["Saldo nach Buchung"].str.replace(",", ".").astype(float)

        # Füge die x- und y-Werte zur entsprechenden Liste hinzu
        x_values.extend(data["Buchungstag"])
        y_values.extend(data["Saldo nach Buchung"])

    # Erstelle den Plot des Kontostands für alle Daten
    plt.plot(x_values, y_values)
    plt.xlabel("Buchungstag")
    plt.ylabel("Saldo nach Buchung")
    plt.title("Kontostand über alle Daten")
    plt.xticks(rotation=45)
    plt.show()


root = tk.Tk()
root.title("Finance Explorer")  # Titel des Fensters

label = tk.Label(root, text="Willkommen zum Finance Explorer")
label.pack()  # Platziere das Label im Hauptfenster

button = tk.Button(root, text="xy chart selected month", command=button_click) 
button.pack()  # Platziere den Button im Hauptfenster

button = tk.Button(root, text="pie chart", command=show_cost_pie_chart) 
button.pack()  # Platziere den Button im Hauptfenster

button = tk.Button(root, text="xy chart all data", command= show_kontostand_all_plot)
button.pack()


# Dropdown-Liste erstellen und mit den Dateinamen füllen
dropdown = ttk.Combobox(root, values=csv_files)
dropdown.current(0)
dropdown.pack()

root.mainloop()