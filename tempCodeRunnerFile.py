import tkinter as tk
import math

# --- Calculator Functions ---
def press(num):
    entry_var.set(entry_var.get() + str(num))

def clear():
    entry_var.set("")

def delete():
    entry_var.set(entry_var.get()[:-1])

def equal():
    try:
        expression = entry_var.get()
        result = str(eval(expression))  # evaluates the expression safely
        entry_var.set(result)
    except ZeroDivisionError:
        entry_var.set("Error: Division by 0")
    except Exception:
        entry_var.set("Error")

def square_root():
    try:
        value = float(entry_var.get())
        entry_var.set(str(math.sqrt(value)))
    except Exception:
        entry_var.set("Error")

def power():
    entry_var.set(entry_var.get() + "**")

def percentage():
    try:
        value = float(entry_var.get())
        entry_var.set(str(value / 100))
    except Exception:
        entry_var.set("Error")

# --- GUI Setup ---
root = tk.Tk()
root.title("✨ Advanced Calculator ✨")
root.geometry("350x500")
root.resizable(False, False)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, pady=10)

# --- Button Layout ---
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("⌫", 5, 1), ("√", 5, 2), ("^", 5, 3),
    ("=", 6, 0)
]

# --- Create Buttons ---
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=30, height=2, command=equal, bg="lightgreen")
        btn.grid(row=row, column=col, columnspan=4, pady=5)
    elif text == "C":
        btn = tk.Button(root, text=text, width=7, height=2, command=clear, bg="lightcoral")
        btn.grid(row=row, column=col, pady=5)
    elif text == "⌫":
        btn = tk.Button(root, text=text, width=7, height=2, command=delete, bg="orange")
        btn.grid(row=row, column=col, pady=5)
    elif text == "√":
        btn = tk.Button(root, text=text, width=7, height=2, command=square_root, bg="lightblue")
        btn.grid(row=row, column=col, pady=5)
    elif text == "^":
        btn = tk.Button(root, text=text, width=7, height=2, command=power, bg="lightblue")
        btn.grid(row=row, column=col, pady=5)
    elif text == "%":
        btn = tk.Button(root, text=text, width=7, height=2, command=percentage, bg="lightblue")
        btn.grid(row=row, column=col, pady=5)
    else:
        btn = tk.Button(root, text=text, width=7, height=2, command=lambda t=text: press(t))
        btn.grid(row=row, column=col, pady=5)

root.mainloop()
