import tkinter as tk

root = tk.Tk()

def window_configs():
    root.title("Sonipy")
    root.configure(bg="#1c1b22")
    root.minsize(720, 480)
    root.maxsize(1920, 1080)
    

    

def window_built():
    window_configs() 
    root.mainloop()