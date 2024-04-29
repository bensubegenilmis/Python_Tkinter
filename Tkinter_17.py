#Date Picker

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def secilenTarih():
    secilen_tarih = tarih.get_date()
    print(f"Seçilen tarih: {secilen_tarih}")

tarih = Calendar(
    pencere,
    selectmode="day",  #selectmode="day" belirterek, kullanıcının yalnızca bir gün seçebileceğini belirtiyoruz. 
    date_pattern="dd/MM/yyyy"  #tarih biçimini belirtiyoruz
)
tarih.pack()

button = tk.Button(pencere, text="Tarih Seç", command=secilenTarih)
button.pack()


pencere.mainloop()