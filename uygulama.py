import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import Tc_Dogrulama

form = tk.Tk()

form.geometry("300x300")
form.config(bg="black")
form.title("Arıza Bildirim Uygulaması")
lbl_baslık = tk.Label(form, text="Arıza Bildirim Uygulaması", bg="black", fg="white", font="Times 17 bold")

lbl_baslık.pack(pady=(10))

kullanici_adi = tk.StringVar()
sifre = tk.StringVar()

lbl_ad = tk.Label(form, text="Kullanıcı adı : ", bg="black", fg="white", font="Times 11 bold italic")
lbl_ad.place(x=20, y=90)

lbl_sifre = tk.Label(form, text="Şifre : ", bg="black", fg="white", font="Times 11 bold italic")
lbl_sifre.place(x=20, y=130)

entry_ad = tk.Entry(form)
entry_ad.place(x=120, y=90)
entry_sifre = tk.Entry(form, show="*")
entry_sifre.place(x=120, y=130)


def giris():
    if entry_ad.get() == "bensu" and entry_sifre.get() == "1234":
        msg = messagebox.showinfo("Tebrikler", message="Giriş Başarılı")
        if msg == "ok":
            basvuru_formu = tk.Toplevel()
            basvuru_formu.geometry("350x350")
            basvuru_formu.title("Arıza Bildirim Formu")
            basvuru_formu.config(bg="yellow")
            baslik_label = tk.Label(basvuru_formu, text="Arıza Bildirim Formu", bg="yellow", fg="red",
                                    font="Times 20 bold")
            baslik_label.pack()

            label_ad = tk.Label(basvuru_formu, text="Ad-Soyad : ", font="consoles 12 italic", bg="yellow",
                                fg="black").place(x=40, y=50)
            label_tc_no = tk.Label(basvuru_formu, text="Tc No : ", font="consoles 12 italic", bg="yellow",
                                   fg="black").place(x=40, y=90)
            label_modem_tipi = tk.Label(basvuru_formu, text="Modem Tipi : ", font="consoles 12 italic", bg="yellow",
                                        fg="black").place(x=40, y=130)
            label_ariza_tipi = tk.Label(basvuru_formu, text="Arıza Tipi : ", font="consoles 12 italic", bg="yellow",
                                        fg="black").place(x=40, y=170)
            label_adres = tk.Label(basvuru_formu, text="Adres : ", font="consoles 12 italic", bg="yellow",
                                   fg="black").place(x=40, y=210)
            label_mail = tk.Label(basvuru_formu, text="Mail : ", font="consoles 12 italic", bg="yellow",
                                  fg="black").place(x=40, y=250)

            entry_ad_soyad = tk.Entry(basvuru_formu)
            entry_ad_soyad.place(x=140, y=50)

            entry_tc_no = tk.Entry(basvuru_formu)
            entry_tc_no.place(x=140, y=90)

            liste = ["TMP", "KMNR", "2TMNx", "MTPL", "NMPY", "PNDAS"]
            combo_modem = Combobox(basvuru_formu, values=liste)
            combo_modem.place(x=140, y=130)

            liste1 = ["Kablo Arızalı", "Giriş Arızalı", "Wifi Açılmıyor", "İnternet Çekmiyor", "İnternet hızı yavaş",
                      "İnternet çekmiyor"]
            combo_ariza_tipi = Combobox(basvuru_formu, values=liste1)
            combo_ariza_tipi.place(x=140, y=170)

            entry_adres = tk.Entry(basvuru_formu)
            entry_adres.place(x=140, y=250)

            entry_mail = tk.Entry(basvuru_formu)
            entry_mail.place(x=140, y=210)

            def olustur():
                kosul = Tc_Dogrulama.Tc(entry_tc_no.get())

                if kosul == True:
                    msgm = messagebox.showinfo("Başarıyla oluştu", message="Arıza Bildirimi Gerçekleştirildi")
                else:
                    messagebox.showinfo("Başarısız", "Tc Kimlik numaranızı doğru girdiğinize emin olunuz ")

            buton = tk.Button(basvuru_formu, text="Oluştur", command=olustur).place(x=140, y=290)

            basvuru_formu.mainloop()


def iptal():
    pass


btn_giris = tk.Button(form, text="Giriş", activebackground="green", command=giris)
btn_iptal = tk.Button(form, text="İptal", activebackground="red", command=iptal)

btn_giris.place(x=120, y=180, width=60)
btn_iptal.place(x=190, y=180, width=60)

