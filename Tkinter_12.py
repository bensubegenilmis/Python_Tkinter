# Text Editor

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

metin = tk.Text(
    bilesen2,
    width=40,
    height=10,
    wrap=tk.WORD  #wrap=tk.WORD parametresi, metin kutusunun satır sonlarında otomatik olarak kelime bölmesi yapmasını sağlar. 
) 
metin.pack(fill=tk.BOTH, expand=True)  #fill=tk.BOTH parametresi, bileşenin hem yatayda hem de dikeyde alanı doldurmasını sağlar. expand=True parametresi, bileşenin kullanılabilir alanda genişlemesini sağlar.

def metinFonksiyonu():
    print(metin.get(1.0, tk.END))  # İlk satırdan (1.0) başlayarak, tüm metni almak için tk.END ifadesi kullanılır.

buton = tk.Button(bilesen2, text="Kaydet", command=metinFonksiyonu)
buton.pack(pady=10)

pencere.mainloop()