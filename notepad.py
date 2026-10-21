
from tkinter import *
from tkinter import filedialog, messagebox

def new_file():
    text.delete("1.0", END)

def open_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        f = open(file, "r")
        text.delete("1.0", END)
        text.insert("1.0", f.read())
        f.close()

def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if file:
        f = open(file, "w")
        f.write(text.get("1.0", END))
        f.close()
        messagebox.showinfo("Success", "File Saved Successfully!")

def clear_text():
    if text.get("1.0", END).strip() == "":
        messagebox.showwarning("Warning", "Notepad is already empty!")
    else:
        text.delete("1.0", END)

root = Tk()
root.title("My Notepad")
root.geometry("600x400")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear All", command=clear_text)

text = Text(root, font=("Arial", 12), undo=True)
text.pack(expand=True, fill="both")

root.mainloop()
