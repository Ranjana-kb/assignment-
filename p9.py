"""
QN: Write Python GUI program to take the birth date and output the age when a
button is pressed. (JUNE 2022)
"""
from tkinter import *
from datetime import datetime

def calculate_age():
    birth_date = entry.get()  
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")  
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid Date! Use YYYY-MM-DD format.")


root = Tk()
root.title("Age Calculator")
root.geometry("300x200")


Label(root, text="Enter Birth Date (YYYY-MM-DD):").pack(pady=5)
entry = Entry(root)
entry.pack(pady=5)


Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)


result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()j
