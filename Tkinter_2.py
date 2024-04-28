#Pack Manager: Bu yönetim mekanizması, bileşenleri dikey veya yatay olarak paketleyerek yerleştirir. Bileşenler, eklenme sırasına göre otomatik olarak sıralanır ve mevcut boş alana göre genişletilir.
#Grid Manager: Bu yönetim mekanizması, bileşenleri bir ızgara düzeni şeklinde yerleştirir. Bileşenler, satır ve sütun indeksleri kullanılarak belirli hücrelere yerleştirilir. Bu yönetim mekanizması, bileşenlerin esnek bir şekilde yerleştirilmesini ve hücre boyutlarının ayarlanmasını sağlar.
#Place Manager: Bu yönetim mekanizması, bileşenleri doğrudan belirli bir konuma yerleştirir. Bileşenlerin koordinatları (x, y) cinsinden belirlenir. Bu yönetim mekanizması, daha hassas yerleştirme ve hizalama gerektiren durumlar için kullanılabilir.


#Pack Manager
# import tkinter as tk
# from tkinter import ttk

# pencere = tk.Tk()
# pencere.geometry("600x450")
# pencere.title("Uygulamaya Hoş Geldiniz!")

# buton_sol_1 = tk.Button(pencere, text="Buton1", fg="red")
# buton_sol_1.pack(side=tk.LEFT)  #Düğmeyi pencerenin sol tarafına yerleştirir.

# buton_sol_2 = tk.Button(pencere, text="Buton2", fg="red")
# buton_sol_2.pack(side=tk.LEFT)

# buton_ust_1 = tk.Button(pencere, text="Buton3", fg="orange")
# buton_ust_1.pack(side=tk.TOP) #Düğmeyi pencerenin üst tarafına yerleştirir.

# buton_ust_2 = tk.Button(pencere, text="Buton4", fg="orange")
# buton_ust_2.pack(side=tk.TOP)

# btn_alt_1 = tk.Button(pencere, text="Buton5", fg="blue")
# btn_alt_1.pack(side=tk.BOTTOM) #Düğmeyi pencerenin alt tarafına yerleştirir.

# btn_alt_2 = tk.Button(pencere, text="Buton6", fg="blue", bg="gray")
# btn_alt_2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# #fill=tk.BOTH: Bu parametre, paketlenen bileşenin ebeveyn bileşenin hem yatay (x ekseni) hem de dikey (y ekseni) yönde genişlemesini sağlar.

# #expand=True: Bu parametre, paketlenen bileşenin ebeveyn bileşenin kullanılmayan boş alanlarını doldurması gerektiğini belirtir. 
 
# pencere.mainloop()

#Grid Manager

# import tkinter as tk
# from tkinter import ttk

# pencere = tk.Tk()
# pencere.title("Uygulamaya Hoş Geldiniz!")

# for satir in range(1,16):  # 1'den 15'e kadar olan satırlar için bir döngü oluşturur
#     for sutun in range(1,11): # 1'den 10'a kadar olan sütunlar için bir döngü oluşturur.
#         etiket = tk.Label(pencere, text='Satır%s-Sütun%s'%(satir,sutun))  #Her döngüde bir etiket oluşturur. Etiketin metni, döngüdeki satır ve sütun numarasını içerir.
#         etiket.grid(row=satir, column=sutun, padx=5, pady=5) 

# pencere.mainloop()

# Place Manager

import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.title("Uygulamaya Hoş Geldiniz!")

etiket1 = tk.Label(pencere, text="Etiket1")
etiket1.place(x = 25, y = 25)  #Etiketi yatay ve dikey eksenden 25 piksel olacak şekilde uzaklaştırma

etiket2 = tk.Label(pencere, text="Etiket2")
etiket2.place(relx = 0.5, rely = 0.5)  #tam ortaya almak için 0.5 değerini (%50) vermeliyiz

pencere.mainloop()
