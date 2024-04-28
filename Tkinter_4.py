import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

def butonFonksiyonu():
    cb = acilir_kutu.get()

    if cb == "İstanbul":
        print("İstanbul seçildi")
    elif cb == "Ankara":
        print("Ankara seçildi")
    elif cb == "İzmir":
        print("İzmir seçildi")

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

acilir_kutu = tk.StringVar()  #acilir_kutu isminde bir StringVar oluşturuyoruz.Bu değişken, depolama için kullanılacak.
acilir_kutu = ttk.Combobox(
    pencere,
    textvariable=acilir_kutu,  #textvariable, seçilen değeri depolamak için kullanılacak olan acilir_kutu değişkenine atar.
    values=("İstanbul","Ankara","İzmir"), #gösterilecek seçenekleri belirtir
    state="readonly"  # kullanıcının elle bir değer giremeyeceği, yalnızca mevcut seçenekler arasından seçim yapabileceği anlamına gelir.
)
acilir_kutu.place(relx=0.4, rely=0.3)

pencere.mainloop()