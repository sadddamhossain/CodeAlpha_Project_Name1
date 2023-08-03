#!/usr/bin/env python
# coding: utf-8

# # CURRENCY CONVERTER Python Model

# In[4]:


import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x200")

        self.c = CurrencyRates()

        self.from_currency_label = tk.Label(root, text="From Currency:")
        self.from_currency_label.pack()

        self.from_currency_var = tk.StringVar()
        self.from_currency_dropdown = tk.OptionMenu(root, self.from_currency_var, *self.c.get_rates('USD').keys())
        self.from_currency_dropdown.pack()

        self.to_currency_label = tk.Label(root, text="To Currency:")
        self.to_currency_label.pack()

        self.to_currency_var = tk.StringVar()
        self.to_currency_dropdown = tk.OptionMenu(root, self.to_currency_var, *self.c.get_rates('USD').keys())
        self.to_currency_dropdown.pack()

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def convert_currency(self):
        try:
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            amount = float(self.amount_entry.get())

            converted_amount = self.c.convert(from_currency, to_currency, amount)
            self.result_label.config(text=f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        except Exception as e:
            self.result_label.config(text="Conversion Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()


# In[ ]:





# In[ ]:




