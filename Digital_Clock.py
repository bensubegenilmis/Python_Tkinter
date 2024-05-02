import tkinter as tk
import time

form = tk.Tk()
form.title("Uygulama")
form.geometry("250x200+500+250")
form.config(bg="yellow")

def zaman():
    zaman_format = time.strftime("%H:%M:%S")
    zmn_label.config(text=zaman_format)
    zmn_label.after(200, zaman)  # Corrected line

zmn_label = tk.Label(form, bg="white", font="Times 35 bold")
zmn_label.place(x=30, y=80)
zaman()

baslik=tk.Label(text="Digital Clock", font="Times 15 bold", bg="yellow", )
baslik.pack(pady=10)

form.mainloop()
