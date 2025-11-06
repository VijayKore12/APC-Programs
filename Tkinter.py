import tkinter as tk


window = tk.Tk()
window.title("My First Tkinter Window")
window.geometry("300x200")   


label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)


def on_click():
    label.config(text="Button Clicked!")

button = tk.Button(window, text="Click Me", command=on_click)
button.pack(pady=10)


window.mainloop()
