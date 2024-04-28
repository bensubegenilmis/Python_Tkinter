#Check Button

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

def butonFonksiyonu():
    print("Gönderildi.")

buton = tk.Button(
    pencere,
    text="Tıkla",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="black",
    font=24,
    height=2,
    width=10,
    cursor="hand2",
    command= butonFonksiyonu
)
buton.place(relx=0.4,rely=0.1)

def gonderFonksiyonu():
    yazilim = onay_kutusu_degisken.get()

    if yazilim == 1:
        print("Yazılım eklendi.")
    else:
        print("Yazılım eklenmedi.")

onay_kutusu_degisken = tk.IntVar() #tk.IntVar() ile bir Tkinter değişkeni oluşturduk
onay_kutusu_degisken.set(0)  #değişkenini başlangıçta seçilmemiş olarak ayarladık
onay_kutusu = tk.Checkbutton(
    pencere,
    text="Yazılım departmanına da gönder",
    variable=onay_kutusu_degisken,
    activebackground="orange",
    activeforeground="black",
    command=gonderFonksiyonu
)
onay_kutusu.place(relx=0.4, rely=0.3)

pencere.mainloop()