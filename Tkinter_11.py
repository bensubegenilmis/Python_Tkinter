#Listbox

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

bilesenler = ttk.Notebook(
    pencere,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen1 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)

grafik = tk.Label(
    bilesen1,
    text="Grafik"
)
grafik.pack()

tablo = tk.Label(
    bilesen2,
    text="Tablo"
)
tablo.pack()

bilesenler.add(
    bilesen1,
    text="Grafik"
)

bilesenler.add(
    bilesen2,
    text="Tablo"
)

liste = tk.Listbox(bilesen2, selectmode=tk.MULTIPLE)

liste.insert(0, "Python")
liste.insert(1, "Java")

liste.place(x=5, y=5)

def listeOgeleri():
    liste_indeks = liste.curselection()
    print(liste_indeks)

    for l in liste_indeks:
        print(liste.get(l))

buton = tk.Button(
    bilesen2,
    text="Seç",
    command=listeOgeleri
)
buton.place(x=50, y=180)

pencere.mainloop()