import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("App")
root.geometry("400x400")
label = tk.Label(root, text="First Tkinter!", font=(16))
#label.pack(pady=20)
label.grid()
root.mainloop()