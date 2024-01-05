import tkinter as tk
import pyperclip

def paste(event):
    text = event.widget.cget("text")
    pyperclip.copy(text)

def button_click(event):
    new_button = tk.Button(root, text="Copy")
    new_button.pack(pady=10)
    new_button.bind("<Button-1>", button_click)
    clipboard_content = pyperclip.paste()
    event.widget.config(text = clipboard_content)
    event.widget.bind("<Button-1>", paste)


# Create the main window
root = tk.Tk()
root.title("Simple GUI")



# Create a button
button = tk.Button(root, text="Copy", command=button_click)
button.pack(pady=10)

button.bind("<Button-1>", button_click)

# Run the main loop
root.mainloop()
