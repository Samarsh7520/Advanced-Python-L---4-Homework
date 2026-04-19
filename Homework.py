import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

app = tk.Tk()
app.title("Random Password Generator")
app.geometry("350x200")

tk.Label(app, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(app)
length_entry.insert(0, "12")
length_entry.pack()

generate_btn = tk.Button(app, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

result_entry = tk.Entry(app, font=('Arial', 12), width=25)
result_entry.pack(pady=5)

app.mainloop()