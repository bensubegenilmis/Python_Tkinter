import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

def butonFonksiyonu():  #Butona tıkladığımızda hangisini seçtiysek ekrana bastıralım.
    rb = radyo_buton.get()
    if rb == "1":
        print("Radyo Buton 1")
    elif rb == "2":
        print("Radyo Buton 2")

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

buton.pack(pady=10)

radyo_buton = tk.StringVar()  #tk.StringVar() kullanarak bir StringVar nesnesi olan radyo_butonu oluşturduk.
radyo_buton.set("1")  #1" seçeneği başlangıçta seçili olarak ayarlanacak.
radyo_buton1 = tk.Radiobutton(
    pencere,
    text="Radyo Buton 1",
    value="1",
    variable=radyo_buton
)
radyo_buton1.place(x=180, y=135)  #konumlandırmayı yapıyoruz.

radyo_buton2 = tk.Radiobutton(
    pencere,
    text="Radyo Buton 2",
    value="2",
    variable=radyo_buton
)
radyo_buton2.place(x=370, y=135)  #konumlandırmayı yapıyoruz.

pencere.mainloop()