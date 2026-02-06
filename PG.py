import random
import string
import tkinter as tk

root =tk.Tk()
root.title("Password Generator")

characters = string.ascii_letters + string.digits
def click():
        password = ''.join(random.choices(characters,k= 10)) 
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
button =tk.Button(root,text ="click",command= click).pack(pady=5)
password_entry = tk.Entry(root,width = 35)
password_entry.pack(pady=5)
def copy():
        root.clipboard_clear()
        root.clipboard_append(password_entry.get())
button =tk.Button(root,text="COPY",command=copy).pack(pady=5)
root.mainloop()