Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> from tkinter import ttk
>>> from tkinter import messagebox
>>> 
>>> # Function to perform Caesar Cipher encryption/decryption
... def caesar_cipher(text, shift, direction):
...     result = ""
...     for char in text:
...         if char.isalpha():
...             # Check if character is uppercase or lowercase
...             shift_base = 65 if char.isupper() else 97
...             if direction == "encrypt":
...                 result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
...             elif direction == "decrypt":
...                 result += chr((ord(char) - shift - shift_base) % 26 + shift_base)
...         else:
...             # If character is not alphabetic, add it to result as is
...             result += char
...     return result
... 
>>> 
>>> # Function to handle button click event
... def perform_action():
...     message = message_entry.get()
...     shift = shift_entry.get()
...     action = action_var.get()
...     # Validate inputs
...     if not message or not shift:
...         messagebox.showwarning("Input Error", "Please enter both the message and shift value.")
...         return
...     try:
...         shift = int(shift)
...     except ValueError:
...         messagebox.showwarning("Input Error", "Shift value must be an integer.")
...         return
...     # Perform encryption or decryption
    if action == "Encrypt":
        result = caesar_cipher(message, shift, "encrypt")
    elif action == "Decrypt":
        result = caesar_cipher(message, shift, "decrypt")
    else:
        messagebox.showwarning("Input Error", "Please choose either Encrypt or Decrypt.")
        return
    # Display the result
    result_label.config(text=f"Result: {result}")

    

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
''

# Create and place widgets
ttk.Label(root, text="Enter your message:").grid(row=0, column=0, padx=10, pady=10)
message_entry = ttk.Entry(root, width=50)
message_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(root, text="Enter shift value:").grid(row=1, column=0, padx=10, pady=10)
shift_entry = ttk.Entry(root, width=10)
shift_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')


# Radio buttons for choosing action
action_var = tk.StringVar(value="Encrypt")
ttk.Radiobutton(root, text="Encrypt", variable=action_var, value="Encrypt").grid(row=2, column=0, padx=10, pady=10)
ttk.Radiobutton(root, text="Decrypt", variable=action_var, value="Decrypt").grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Button to trigger action
ttk.Button(root, text="Perform Action", command=perform_action).grid(row=3, column=0, columnspan=2, pady=10)

# Label to display result
result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
