import tkinter
from tkinter import *
from PIL import Image, ImageTk
import pymysql
db=pymysql.connect(host='localhost',user='root',password="ammu",database="registration")
cursor=db.cursor()

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

# Load the background image using PIL
image_path = "D:/Athira/Python/gui/pngtree-modern-double-color-futuristic-neon-background-image_351866 (1).jpg"
image = Image.open(image_path)


label_result = Label(root, text="", font=("bold", 12), fg="green")
label_result.place(x=180, y=420)


#create_table_query = """ create table regis14(FullName varchar(255),Email varchar(255),Gender varchar(255),Age varchar(255))"""

def register():
    try:
        name = entry_1.get()
        email = entry_2.get()
        
        # Retrieve the selected gender from the IntVar
        gender = "Male" if var.get() == 1 else "Female"

        age = entry_3.get()
        print(name)

        insert_query = "INSERT INTO regis13(FullName, Email, Gender, Age) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (name, email, gender, age))
        db.commit()
        label_result.config(text="Registration successful!")

    except Exception as e:
        db.rollback()  # Rollback changes if an exception occurs
        label_result.config(text=f"Error: {str(e)}")

# Create a Tkinter PhotoImage from the PIL image
bg_image = ImageTk.PhotoImage(image)

label_bg = Label(root, image=bg_image)
label_bg.place(relwidth=1, relheight=1)

label_0 = Label(root, text="Registration form", width=16, font=("bold", 20),  bg='white' )
label_0.place(x=90, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10), bg=None)
label_1.place(x=65, y=130)

entry_1 = Entry(root)
entry_1.place(x=240, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10),  bg=None)
label_2.place(x=68, y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y=180)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10), bg=None)
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Male", padx=8, variable=var, value=1,  bg=None).place(x=240, y=230)
Radiobutton(root, text="Female", padx=20, variable=var, value=2, bg=None).place(x=290, y=230)

label_4 = Label(root, text="Age:", width=20, font=("bold", 10), bg=None)
label_4.place(x=70, y=280)

entry_3 = Entry(root)
entry_3.place(x=240, y=280)

Button(root, text='Submit',command=register,width=20, bg='brown', fg='white').place(x=180, y=380)


# it is used for displaying the registration form on the window
root.mainloop()
print("registration form successfully created...")
