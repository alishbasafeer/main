from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import messagebox

c = CurrencyConverter()

window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

def clicked():
    try:
        amount = float(entry_amount.get())
        cur1 = entry_from.get().upper()
        cur2 = entry_to.get().upper()
        data = c.convert(amount, cur1, cur2)
        label_result.config(text=f"{amount} {cur1} = {data:.2f} {cur2}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear():
    entry_amount.delete(0, tk.END)
    entry_from.delete(0, tk.END)
    entry_to.delete(0, tk.END)
    label_result.config(text="")

label_title = tk.Label(window, text="Currency Converter", font="times 20 bold")
label_title.grid(row=0, column=0, columnspan=2, pady=20)

label_amount = tk.Label(window, text="Enter amount here:", font="times 16")
label_amount.grid(row=1, column=0, padx=20, pady=10, sticky='e')
entry_amount = tk.Entry(window)
entry_amount.grid(row=1, column=1, padx=20, pady=10, sticky='w')

label_from = tk.Label(window, text="Enter your currency here:", font="times 16")
label_from.grid(row=2, column=0, padx=20, pady=10, sticky='e')
entry_from = tk.Entry(window)
entry_from.grid(row=2, column=1, padx=20, pady=10, sticky='w')

label_to = tk.Label(window, text="Enter your desired currency:", font="times 16")
label_to.grid(row=3, column=0, padx=20, pady=10, sticky='e')
entry_to = tk.Entry(window)
entry_to.grid(row=3, column=1, padx=20, pady=10, sticky='w')

button_convert = tk.Button(window, text="Convert", font="times 16 bold", command=clicked)
button_convert.grid(row=4, column=0, padx=20, pady=20)

button_clear = tk.Button(window, text="Clear", font="times 16 bold", command=clear)
button_clear.grid(row=4, column=1, padx=20, pady=20)

label_result = tk.Label(window, text="", font="times 16 bold")
label_result.grid(row=5, column=0, columnspan=2, pady=20)

window.mainloop()
