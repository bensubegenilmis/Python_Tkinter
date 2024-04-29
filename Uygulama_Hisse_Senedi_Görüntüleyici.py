import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates

window = tk.Tk()
window.title("Stock Viewer")
window.geometry("950x600")

def show_data():
    # Verileri oku
    symbol = entry_symbol.get()
    start_date = calendar_start.get_date()
    end_date = calendar_end.get_date()
    try:
        # Hisse senedi verilerini al
        data = yf.download(symbol, start=start_date, end=end_date)
        df = pd.DataFrame(data)

        # Tarih sütununu ekle ve formatı çevir
        df.reset_index(inplace=True)
        df["Date"] = pd.to_datetime(df["Date"])

        # Satırları sayısal değerlere dönüştür ve yuvarla
        df[["Open", "High", "Low", "Close", "Adj Close"]] = df[["Open", "High", "Low", "Close", "Adj Close"]].round(1).astype(float)
        df[["Volume"]] = df[["Volume"]].astype(int)

        # Başka bir sembol girildiğinde tabloyu temizle
        table.delete(*table.get_children())

        # Tabloya verileri yerleştir
        table["columns"] = list(df.columns)
        for column in list(df.columns):
            table.column(column, width=100, anchor="center")
            table.heading(column, text=column, anchor="center")
        for index, row in df.iterrows():
            table.insert("", "end", values=list(row))

        # Grafik oluştur
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        ax.plot(df["Date"], df["Close"], linestyle="-", color="red")
        ax.set_xlabel("")
        ax.set_ylabel("Close Price")
        ax.set_title(f"{symbol} Stock Price")

        # Grafik üzerindeki verileri göstermek için Canvas kullan
        canvas = FigureCanvasTkAgg(fig, master=tab_graph)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Eğer daha önce bir grafik eklenmişse önceki grafiği temizle
        for widget in tab_graph.winfo_children():
            widget.destroy()

        # Yeni grafik widget'ını ekle
        canvas = FigureCanvasTkAgg(fig, master=tab_graph)
        canvas.draw()
        canvas.get_tk_widget().pack()

    except Exception as e:
        messagebox.showerror("Error", str(e))

def export_data():
    pass

frame_left = tk.Frame(window)
frame_left.pack(side="left", padx=10, pady=10)

label_symbol = tk.Label(frame_left, text="Stock Symbol:")
label_symbol.pack()

entry_symbol = tk.Entry(frame_left)
entry_symbol.pack()

date_start = tk.Label(frame_left, text="Start Date:")
date_start.pack()
calendar_start = DateEntry(frame_left, width=12, background="darkblue", foreground="white", borderwidth=2)
calendar_start.pack()

date_end = tk.Label(frame_left, text="End Date:")
date_end.pack()
calendar_end = DateEntry(frame_left, width=12, background="darkblue", foreground="white", borderwidth=2)
calendar_end.pack()

button_show = tk.Button(frame_left, text="Show Data", command=show_data)
button_show.pack(pady=10)

button_export = tk.Button(frame_left, text="Export Data", command=export_data)
button_export.pack(pady=10)

tab_control = ttk.Notebook(window)
tab_table = ttk.Frame(tab_control)
tab_control.add(tab_table, text="Table")

tab_graph = ttk.Frame(tab_control)
tab_control.add(tab_graph, text="Graph")

tab_control.pack(expand=1, fill="both")

table = ttk.Treeview(tab_table)
table.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(tab_table, orient="vertical", command=table.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

table.configure(yscrollcommand=scrollbar.set)
table["show"] = "headings"

tab_table.grid_columnconfigure(0, weight=1)
tab_table.grid_rowconfigure(0, weight=1)

window.mainloop()