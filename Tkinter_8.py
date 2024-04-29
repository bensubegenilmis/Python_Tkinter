#Menu

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

def dosyaFonksiyonu():
    print("Yeni Dosya")

def kaynakFonksiyonu():
    print("Veri")

menu_cubugu = tk.Menu(pencere)  #Menu sınıfını kullandık ve bunu pencere nesnesine ekledik.
pencere.config(menu=menu_cubugu)

dosya = tk.Menu(menu_cubugu)  #iki alt menü oluşturduk
kaynak = tk.Menu(menu_cubugu)

menu_cubugu.add_cascade(label="Dosya", menu=dosya)  #alt menüleri ekledik
menu_cubugu.add_cascade(label="Kaynak", menu=kaynak)

dosya.add_command(label="Yeni Dosya", command=dosyaFonksiyonu) #"Dosya" alt menüsüne "Yeni Dosya" isminde bir komut ekledik
kaynak.add_command(label="Veri", command=kaynakFonksiyonu) #"Kaynak" alt menüsüne "Veri" isminde bir komut ekledik

pencere.mainloop()