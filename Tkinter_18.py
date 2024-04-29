#Drag & Drop

#Sürükle bırak yöntemi


from tkinter import *

pencere = Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")
pencere.geometry("600x450")

def surukleBasla(event):  #bir fare tıklaması başladığında çalışacak olan bir olay işleyicidir

#Fonksiyon, tıklanan bileşenin başlangıç konumunu kaydeder.

    bilesen = event.widget  # olayın gerçekleştiği bileşeni temsil eder.
    bilesen.baslaX = event.x #fare tıklamasının x koordinatını temsil eder
    bilesen.baslaY = event.y #fare tıklamasının y koordinatını temsil eder.

def surukleHareket(event):  #fare sürüklendiğinde çalışacak olan bir olay işleyicidir
    bilesen = event.widget # olayın gerçekleştiği bileşeni temsil eder.
    x = bilesen.winfo_x() - bilesen.baslaX + event.x
    #bileşenin mevcut x konumunu temsil eder.
    #bilesen.baslaX ifadesi, bileşenin sürükleme işlemi başladığındaki başlangıç x konumunu temsil eder. event.x ifadesi, fare sürükleme hareketinin anlık x konumunu temsil eder.

    #Yeni bileşen konumunu şu şekilde hesaplarız: Yeni x konumu: mevcut x konumu - başlangıç x konumu + fare sürükleme hareketinin anlık x konumu, Yeni y konumu: mevcut y konumu - başlangıç y konumu + fare sürükleme hareketinin anlık y konumu.

    y = bilesen.winfo_y() - bilesen.baslaY + event.y
    bilesen.place(x=x,y=y)  # ifadesiyle bileşenin yeni konumunu ayarlarız.

etiket = Label(
    pencere,
    bg="red",
    fg="white",
    width=15,
    height=5,
    text="Sürükle Beni",
    font=20
)
etiket.place(x=0, y=0)

etiket.bind("<Button-1>",surukleBasla)
# (Button-1) sol fare düğmesine basıldığında surukleBasla fonksiyonu çalışır.
etiket.bind("<B1-Motion>",surukleHareket)
# etiketin fare sürükleme (B1-Motion) olayına bağlanır.
pencere.mainloop()
