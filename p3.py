"""
QN:Write Python GUI program to input two strings and output a concatenated string
when a button is pressed.(2024 JANUARY)

"""
from tkinter import *
def concatenate_strings():
    str1 = entry1.get()
    str2 = entry2.get()
    result_label.config(text=f"Concatenated String: {str1 + str2}")


root = Tk()
root.title("String Concatenation")
root.geometry("350x200")
root.resizable(False, False)


Label(root, text="Enter First String:").pack(pady=5)
entry1 = Entry(root)
entry1.pack(pady=5)

Label(root, text="Enter Second String:").pack(pady=5)
entry2 = Entry(root)
entry2.pack(pady=5)


Button(root, text="Concatenate", command=concatenate_strings).pack(pady=10)


result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
