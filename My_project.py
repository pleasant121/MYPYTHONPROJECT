import csv
import tkinter as tk
from tkinter import messagebox

# create main window
root = tk.Tk()
root.title("form application")

# Labels and Entries
tk.Label (root, text="Full Name:", font=("Arial", 12)).pack(pady=5)
name_entry = tk.Entry(root, width=30, font=("Arial", 12))
name_entry.pack()

tk.Label(root, text="Email:", font=("Arial", 12)).pack(pady=5)
email_entry = tk.Entry(root, width=30, font=("Arial", 12))
email_entry.pack()

tk.Label(root, text="phone:", font=("Arial", 12)).pack(pady=5)
phone_entry = tk.Entry(root, width=30, font=("Arial", 12))
phone_entry.pack()

tk.Label(root, text="Adress:").pack()
entry_adress = tk.Entry(root, width=30, font=("Arial", 12))
entry_adress.pack()

# fuction to save data to CSV file

def save_data():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    with open('data.csv', 'a',  newline='') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow([name, email, phone])

    messagebox.showinfo("succes", "Dta saved successfully!")

# create the submit button
submit_button = tk.Button(root, text="submit", command=save_data)
submit_button.pack()

# start the main loop
root.mainloop()
