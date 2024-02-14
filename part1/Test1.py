import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide the main window

# Show an information message box
messagebox.showinfo("Information", "This is an information message.")

# Show a warning message box
messagebox.showwarning("Warning", "This is a warning message.")

# Show an error message box
messagebox.showerror("Error", "This is an error message.")

# Ask for user confirmation
result = messagebox.askquestion("Confirmation", "Do you want to proceed?")
if result == 'yes':
    print("User clicked 'Yes'")
else:
    print("User clicked 'No'")

# Ask for user input
user_input = messagebox.askstring("Input", "Enter something:")
print("User input:", user_input)

# Ask for user choice (yes/no/cancel)
choice = messagebox.askyesnocancel("Choice", "Do you want to continue?")
if choice is not None:
    print("User choice:", choice)

root.mainloop()
