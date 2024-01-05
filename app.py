import tkinter as tk
from tkinter import ttk
import pyperclip

def delete(event):
    event.widget.destroy()

def paste(event):
    text = event.widget.cget("text")
    pyperclip.copy(text)

def button_click(event):
    new_button = ttk.Button(root, text="Copy", style='Accent.TButton')
    new_button.pack(pady=10)
    new_button.bind("<Button-3>", button_click)
    clipboard_content = pyperclip.paste()
    event.widget.config(text = clipboard_content, style='')
    event.widget.bind("<Button-3>", paste)
    event.widget.bind("<Button-1>", delete)
    



# Create the main window
root = tk.Tk()
root.title("Clipboard app")
root.geometry("250x500")
root.tk.call('source', 'Forest-ttk-theme/forest-dark.tcl')
ttk.Style().theme_use('forest-dark')


# Create a button
button = ttk.Button(root, text="Copy", style='Accent.TButton')
button.pack(pady=10)

button.bind("<Button-3>", button_click)

# Run the main loop
root.mainloop()
