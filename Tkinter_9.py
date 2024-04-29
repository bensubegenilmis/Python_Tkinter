#Tabs
#Tabs veya sekmeler bileşeni, kullanıcının farklı içerikleri aynı pencerede gruplandırmasına ve sekmeler arasında geçiş yapmasına olanak sağlar.

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

pencere.mainloop()