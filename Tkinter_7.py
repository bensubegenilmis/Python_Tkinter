#Paned Window

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")

bolunmus_pencere_h = ttk.PanedWindow(
    pencere,
    orient=tk.HORIZONTAL
)
bolunmus_pencere_h.pack(fill=tk.BOTH, expand=True)

bolunmus_pencere_v = ttk.PanedWindow(
    bolunmus_pencere_h,
    orient=tk.VERTICAL
)

cerceve_1 = ttk.Frame(
    bolunmus_pencere_h,
    width=600,
    height=200,
    relief=tk.RIDGE #her bir çerçeve farklı bir kenar stiline (relief) sahiptir.
)
cerceve_2 = ttk.Frame(
    bolunmus_pencere_h,
    width=600,
    height=300,
    relief=tk.RAISED
)
bolunmus_pencere_v.add(cerceve_1)
bolunmus_pencere_v.add(cerceve_2)

cerceve_3 = ttk.Frame(
    bolunmus_pencere_h,
    width=240,
    height=500,
    relief=tk.GROOVE
)
bolunmus_pencere_h.add(bolunmus_pencere_v)
bolunmus_pencere_h.add(cerceve_3)

pencere.mainloop()