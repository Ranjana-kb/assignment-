# How do you display an image in a Python GUI? 

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Display Image")

image = Image.open("image.jpg")  # Replace with your image file
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.pack()

root.mainloop()
