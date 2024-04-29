#Mouse Event

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def solTik(event):
    tk.Label(pencere, text="Sol").pack(padx=20, pady=20)

def ortaTik(event):
    tk.Label(pencere, text="Orta").pack(padx=20, pady=20)

def sagTik(event):
    tk.Label(pencere, text="Sağ").pack(padx=20, pady=20)

pencere.bind("<Button-1>", solTik)
pencere.bind("<Button-2>", ortaTik)
pencere.bind("<Button-3>", sagTik)

pencere.mainloop()
