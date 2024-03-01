import tkinter
from tkinter import*
from tkinter import PhotoImage
from tkinter import PhotoImage, Tk
from PIL import Image, ImageTk
root = Tk()
root.geometry('700x700')
root.title("Registration Form")

from tkinter import Label, Tk
from PIL import Image, ImageTk

# Load the image using Pillow
image = Image.open("D:/Athira/Python/gui/pngtree-modern-double-color-futuristic-neon-background-image_351866 (1).jpg")

# Convert the image to PhotoImage
photo_image = ImageTk.PhotoImage(image)

# Create the main window
root = Tk()

# Create a label with the image
label = Label(root, image=photo_image)
label.pack()

# Keep a reference to the image object by attaching it to a widget
label.image = photo_image

# Your remaining code here

root.mainloop()

  


label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=63)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=60,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=60,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=50,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=50,y=280)


entry_2 = Entry(root)
entry_2.place(x=240,y=280)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
