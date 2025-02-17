import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import secrets
import string


def show_popup(passw):
    # Create a main window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show the popup message box
    messagebox.showinfo("Popup", "Your password is: " + passw)
    

def generate_pass():
	
    # Define the alphabet with letters, digits, and symbols
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(int(length.get())))
        
        # Ensure the password contains at least one lowercase letter, one uppercase letter, and at least three digits
        if (any(c.islower() for c in password) 
            and any(c.isupper() for c in password) 
            and sum(c.isdigit() for c in password) >= 3 
            and any(c in "!@#$%^&*()_-+=<>?" for c in password)):  # Check for at least one symbol
            break

    show_popup(str(password))

#window settings
window = tk.Tk()
window.title("Password Generator")
window.geometry("250x150")
window.resizable(False, False)
window.configure(bg = "lavender")

#labels
pass_label = tk.Label(window, text = "Password Length")
pass_label.place(x=30,y=50)

#entryvars
length = tk.StringVar(value = "12")

#entries
length_entry = Entry(window, width=3, textvariable=length)
length_entry.place(x=180,y=50)

#buttons
generate_button = tk.Button(window, text="Generate", bg="whitesmoke", command=generate_pass)
generate_button.place(x=75,y=80)

#start window
window.mainloop()
