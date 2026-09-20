import tkinter as tk

root = tk.Tk()

def window_configs():
    root.title("Sonipy")
    root.configure(bg="black")
    root.minsize(720, 480)
    root.maxsize(1920, 1080)
    

    

def window_built():
    window_configs()  # Apply the configurations    
    root.mainloop()