import tkinter as tk
from tkinter import messagebox

def sil(event):  # Bu fonksiyon, Entry'nin odaklanıldığı zaman çalışacak ve varsayılan metni silerek kullanıcının girdi yapmasını sağlayacak.
    if giris.get() == "Kafanıza göre bir şeyler yazın...":
        giris.delete(0, tk.END) #Entry'deki metni siler.
        giris.config(fg="black") 

def butonFonksiyonu():
    etiket.config(text="Nasılsın?", bg="red", font="Verdana")
    yazdigin_sey = giris.get() # Entry'deki kullanıcı tarafından girilen metni alır.
    etiket.config(text=yazdigin_sey) #Etiketin metnini kullanıcının girdiği metinle günceller.
    giris.config(state="disabled")   #Entry'yi devre dışı bırakır,  kullanıcı daha fazla giriş yapamaz.
    mesaj = messagebox.showinfo(title="Bilgi", message="Butona tıkladın.") #Bilgi mesaj kutusu gösterir.
    print(mesaj)

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulama Hoş Geldiniz!")

buton = tk.Button(
    pencere,
    text="Ben Bir Butonum",
    bg="orange",
    fg="black",
    activebackground="red",
    activeforeground="white",
    font=24,
    height=5,
    width=20,
    cursor="hand2",
    command=butonFonksiyonu
)
buton.pack()

etiket = tk.Label(
    pencere,
    text="Ben Bir Etiketim",
    font="Tahoma 24",
    bg="blue",
    fg="white",
    wraplength=150
)
etiket.pack(pady=10)

giris = tk.Entry(pencere, width=50)
giris.insert(0, "Kafanıza göre bir şeyler yazın...") #arsayılan metin giriş kutusuna eklenir, index 0 olarak 
giris.bind("<FocusIn>", sil)  # Entry odaklandığında ("FocusIn") sil işlevini çağırır.
giris.pack()

pencere.mainloop() #Pencerenin sürekli olarak çalışmasını sağlar
