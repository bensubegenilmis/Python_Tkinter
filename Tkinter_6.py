# import tkinter as tk
# from tkinter import ttk

# pencere = tk.Tk()
# pencere.geometry("600x450")
# pencere.title("Uygulamaya Hoş Geldiniz!")

# sol_cerceve = tk.Frame(
#     pencere,
#     width=400,
#     height=500,
#     bg="gray"
# )
# sol_cerceve.grid(row=0, column=0)

# sag_cerceve = tk.Frame(
#     pencere,
#     width=400,
#     height=500,
#     bg="orange"
# )
# sag_cerceve.grid(row=0, column=1)

# sol_cerceve_1 = tk.Frame(
#     sol_cerceve,
#     width=400,
#     height=300,
#     bg="red"
# )
# sol_cerceve_1.grid(row=0,column=0)

# sol_cerceve_2 = tk.Frame(
#     sol_cerceve,
#     width=400,
#     height=200,
#     bg="blue"
# )
# sol_cerceve_2.grid(row=1,column=0)

# pencere.mainloop()

#Frames

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Uygulamaya Hoş geldiniz!")

sol_cerceve = tk.LabelFrame(
    window,
    width=400,
    height=500,
    bg="gray",
    text="Sol Çerçeve"
)
sol_cerceve.grid(row=0, column=0)

sag_cerceve = tk.LabelFrame(
    window,
    width=400,
    height=500,
    bg="orange",
    text="Sağ Çerçeve"
)
sag_cerceve.grid(row=0, column=1)

sol_cerceve_1 = tk.LabelFrame(
    sol_cerceve,
    width=400,
    height=300,
    bg="red",
    text="Sol Çerçeve Üst"
)
sol_cerceve_1.grid(row=0,column=0)

sol_cerceve_2 = tk.LabelFrame(
    sol_cerceve,
    width=400,
    height=200,
    bg="blue",
    text="Sol Çerçeve Alt"
)
sol_cerceve_2.grid(row=1,column=0)

window.mainloop()