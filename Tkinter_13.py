#Scroll Bar

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

bilesenler = ttk.Notebook(pencere, width=550, height=400)
bilesenler.place(x=25, y=25)

bilesen1 = ttk.Frame(bilesenler, width=50, height=50)
bilesen2 = ttk.Frame(bilesenler, width=50, height=50)

grafik = tk.Label(bilesen1, text="Grafik")
grafik.pack()

tablo = tk.Label(bilesen2, text="Tablo")
tablo.pack()

bilesenler.add(bilesen1, text="Grafik")
bilesenler.add(bilesen2, text="Tablo")

metin = tk.Text(
    bilesen2,
    width=40,
    height=10,
    wrap=tk.WORD
)
metin.pack(fill=tk.BOTH, expand=True)

kaydirma_cubugu = tk.Scrollbar(metin, orient=tk.VERTICAL, command=metin.yview)
#Bu çubuğun yatayda yerine dikey olarak kullanılması için orient=tk.VERTICAL parametresini verdik.command=metin.yview ise kaydırma çubuğunun metin kutusuyla senkronize çalışmasını sağlar.

kaydirma_cubugu.pack(side=tk.RIGHT, fill=tk.Y)

#kaydirma_cubugu.pack(side=tk.RIGHT, fill=tk.Y) ile kaydırma çubuğunu sağ tarafa (side=tk.RIGHT) ve dikeyde (fill=tk.Y) metin kutusunun içine yerleştirdik.

metin.config(yscrollcommand=kaydirma_cubugu.set)
#metin.config(yscrollcommand=kaydirma_cubugu.set) ile metin kutusunu kaydırma çubuğu ile senkronize hale getirdik. Bu sayede kaydırma çubuğu hareket ettikçe metin kutusu da kaydırılır.

def metinFonksiyonu():
    print(metin.get(1.0, tk.END))
    metin.delete(1.0, tk.END)  # Metin kutusunu temizle

buton = tk.Button(bilesen2, text="Kaydet", command=metinFonksiyonu)
buton.pack(pady=10)

pencere.mainloop()