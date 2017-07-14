# -*- coding: utf-8 -*-

import tkinter as tk
import config_service as cs

def present_user_config_form():
    root=tk.Tk()
    root.title("Configure copy/rename script")
    root.geometry("600x200")
    add_buttons(root)
    root.mainloop()
    
def quit_win(root):
    root.destroy()
    
def add_buttons(root):
    tk.Button(root,text="Config", command= lambda: configure(root)).pack()
    tk.Button(root,text="Close", command= lambda: quit_win(root)).pack()
    
def configure(root):
    return True

