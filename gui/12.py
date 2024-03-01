import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Label, Tk
def register():
    # Add your registration logic here
    print("Registration logic goes here")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Load the background image using PIL
image_path = "D:/Athira/Python/gui/pngtree-modern-double-color-futuristic-neon-background-image_351866 (1).jpg"
image = Image.open(image_path)

# Create a Tkinter PhotoImage from the PIL image
bg_image = ImageTk.PhotoImage(image)

# Set the window size to match the background image
root.geometry("{}x{}+{}+{}".format(bg_image.width(), bg_image.height(), 100, 100))

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
canvas.pack()

# Display the background image
canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
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

