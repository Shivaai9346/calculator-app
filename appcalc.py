import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget
entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=8, ipady=8)

# Create a 2D list of button labels
button_labels = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", "=", "/"]
]

# Create and add the buttons
for i in range(4):
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    for j in range(4):
        button = tk.Button(frame, text=button_labels[i][j], font=("Helvetica", 16), relief=tk.RAISED)
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        button.bind("<Button-1>", on_button_click)

# Start the main loop
root.mainloop()
