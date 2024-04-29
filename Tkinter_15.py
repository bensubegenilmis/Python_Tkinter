#Plot

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def plot_zaman_serisi():
    t = np.arange(0, 10, 0.1)
    y = np.random.randn(len(t))

    #.arange fonksiyonunu kullanarak 0'dan 10'a kadar olan sayıları 0.1 aralıklarla içeren bir dizi (t) oluşturuyoruz. Ayrıca, np.random.randn fonksiyonunu kullanarak t dizisinin uzunluğu kadar rasgele sayılardan oluşan bir dizi (y) oluşturuyoruz.


    figure = Figure(figsize=(5, 4), dpi=100)
    plot = figure.add_subplot(111)
    plot.plot(t, y)

    canvas = FigureCanvasTkAgg(figure, master=pencere) #çizimi yapacağınız alanı pencere isimli ana pencereye yerleştiriyoruz. 
    canvas.draw() #yöntemini kullanarak çizimi gerçekleştiriyoruz.
    canvas.get_tk_widget().pack() #anvas öğesini pencereye yerleştiriyoruz.Bu, çizimin gösterildiği bir grafik alanını ekranda görünür hale getirir.

button = ttk.Button(pencere, text="Zaman Serisini Çiz", command=plot_zaman_serisi)
button.pack()

pencere.mainloop()