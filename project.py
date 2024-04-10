import tkinter as tk
from tkinter import ttk

def calculate_loan():
    principal = float(principal_entry.get())
    interest_rate = float(interest_rate_entry.get()) / 100
    years = int(years_entry.get())

    monthly_interest_rate = interest_rate / 12
    months = years * 12

    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)

    result_label.config(text=f"Monthly Payment: {monthly_payment:.2f}")

root = tk.Tk()
root.title("Loan Calculator")

principal_label = ttk.Label(root, text="Principal:")
principal_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
principal_entry = ttk.Entry(root)
principal_entry.grid(row=0, column=1, padx=5, pady=5)

interest_rate_label = ttk.Label(root, text="Annual Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
interest_rate_entry = ttk.Entry(root)
interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)

years_label = ttk.Label(root, text="Years:")
years_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
years_entry = ttk.Entry(root)
years_entry.grid(row=2, column=1, padx=5, pady=5)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_loan)
calculate_button.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
