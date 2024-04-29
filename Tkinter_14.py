# Fie Dialog

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image

pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def dosyaAc():
    dosya = filedialog.askopenfilename(initialdir="C:/Users/Uraz/Desktop", title="Bir dosya seç...")
    #fonksiyonu, bir dosya seçme iletişim kutusu açar ve kullanıcının bir dosya seçmesini bekler.initialdir parametresi belirtilen dizinde başlar
    
    print(dosya)

    resim = Image.open(dosya)  
    resim = ImageTk.PhotoImage(resim)
    
#Eklediğimiz kod, seçilen dosyanın bir resim dosyası olduğunu varsayarak, seçilen resmi açıp görüntülemek için PIL (Python Imaging Library) ve Tkinter'ın Image ve ImageTk modüllerini kullanıyor.

    etiket = tk.Label(pencere, image=resim)
    etiket.image = resim
    etiket.pack(padx=20, pady=20)

buton = tk.Button(
    pencere,
    text="Dosya Aç",
    command=dosyaAc
)
buton.pack()

pencere.mainloop()