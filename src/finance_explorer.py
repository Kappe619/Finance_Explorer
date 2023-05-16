import pandas as pd
import tkinter as tk
#import matplotlib.pyplot as plt

def button_click():
    # Hier kannst du den Code für die Aktion schreiben, die beim Klicken des Buttons ausgeführt werden soll
    # Zum Beispiel: Eine Meldung anzeigen
    label.config(text="Button wurde geklickt!")


root = tk.Tk()
root.title("Finance Explorer")  # Titel des Fensters

label = tk.Label(root, text="Willkommen zum Finance Explorer")
label.pack()  # Platziere das Label im Hauptfenster

button = tk.Button(root, text="Klick mich", command=button_click)  # command=button_click weist dem Button die Funktion button_click() als Aktion zu
button.pack()  # Platziere den Button im Hauptfenster

root.mainloop()


#def button_click():
