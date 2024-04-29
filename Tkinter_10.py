#Treeview

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.geometry("600x450")
pencere.title("Uygulamaya Hoş Geldiniz!")

bilesenler = ttk.Notebook(
    pencere,
    width=550,
    height=400
)
bilesenler.place(x = 25, y = 25)

bilesen1 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)

bilesen2 = ttk.Frame(
    bilesenler,
    width=50,
    height=50
)

grafik = tk.Label(
    bilesen1,
    text="Grafik"
)
grafik.pack()

tablo = tk.Label(
    bilesen2,
    text="Tablo"
)
tablo.pack()

bilesenler.add(
    bilesen1,
    text="Grafik"
)

bilesenler.add(
    bilesen2,
    text="Tablo"
)

agac_yapisi = ttk.Treeview(bilesen2)
agac_yapisi.place(x=10, y=10)

agac_yapisi.insert("", "0", "item1", text="Türkiye")  #(boş bir dize), yeni düğümün ekleneceği düğümün kimliğini belirtir.Boş bir dize verildiğinde, yeni düğümün doğrudan kök düğüm olacağını gösterir.İkinci parametre olan "0", yeni düğümün sıralama indeksini belirtir.Üçüncü parametre olan "item1", yeni düğümün benzersiz bir kimliğini belirtir.text="Türkiye" ifadesi, yeni düğümün görünen metnini belirtir. 
agac_yapisi.insert("item1", "1", "item1_1", text="İstanbul")
agac_yapisi.insert("", "2", "item2", text="Yunanistan")
agac_yapisi.insert("item2", "3", "item2_1", text="Atina")

def callback(event):  #Bu kod parçası, bir olay (event) gerçekleştiğinde (fare tıklaması), callback isimli bir fonksiyonu çağırır.
    item = agac_yapisi.identify("item", event.x, event.y)
    print(item)

agac_yapisi.bind("<Double-1>",callback) 

#bind yöntemi kullanılarak belirli bir olaya (event) belirli bir işlevin (callback) atanması sağlanır.

#"<Double-1>" ifadesi, fare ile çift tıklama olayını temsil eder. Yani, kullanıcı ağaç görünüm bileşeninde bir öğeye çift tıkladığında bu olay tetiklenir.


pencere.mainloop()