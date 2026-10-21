
# from tkinter import *

# def register():
#     name = e1.get()
#     roll = e2.get()
#     course = e3.get()

#     result.config(text="Registration Successful!\nName: " + name +
#                   "\nRoll No: " + roll + "\nCourse: " + course)

# root = Tk()
# root.title("Student Registration Form")
# root.geometry("350x300")

# Label(root, text="Student Registration Form",
#       font=("Arial", 14, "bold")).pack(pady=10)

# Label(root, text="Student Name").pack()
# e1 = Entry(root)
# e1.pack()

# Label(root, text="Roll Number").pack()
# e2 = Entry(root)
# e2.pack()

# Label(root, text="Course").pack()
# e3 = Entry(root)
# e3.pack()

# Button(root, text="Register", command=register).pack(pady=10)

# result = Label(root, text="")
# result.pack()

# root.mainloop()



from tkinter import *
from tkinter import messagebox

def register():
    name = e1.get()
    roll = e2.get()
    course = e3.get()

    if name == "" or roll == "" or course == "":
        messagebox.showerror("Error", "All fields are required!")

    elif not name.isalpha():
        messagebox.showerror("Error", "Name must contain only letters!")

    elif not roll.isdigit():
        messagebox.showerror("Error", "Roll number must contain digits only!")

    else:
        messagebox.showinfo("Success", "Registration Successful!")
        result.config(text="Name: " + name +
                      "\nRoll No: " + roll +
                      "\nCourse: " + course)

root = Tk()
root.title("Student Registration Form")
root.geometry("350x350")

Label(root, text="Student Registration Form",
      font=("Arial", 14, "bold")).pack(pady=10)

Label(root, text="Student Name").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="Roll Number").pack()
e2 = Entry(root)
e2.pack()

Label(root, text="Course").pack()
e3 = Entry(root)
e3.pack()

Button(root, text="Register", command=register).pack(pady=10)

result = Label(root, text="")
result.pack()

root.mainloop()
