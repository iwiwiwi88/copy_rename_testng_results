# -*- coding: utf-8 -*-

import tkinter as tk
import config_service as cs
import copy_test_results as cts

def present_user_config_form():
    root=tk.Tk()
    root.title("Configure copy/rename script")
    root.geometry("600x200")
    add_grid(root)
    root.mainloop()
    
def quit_win(root):
    root.destroy()

def add_grid(root):
    add_labels(root)

    e1 = tk.Entry(root)
    e2 = tk.Entry(root)
    e3 = tk.Entry(root)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    tk.Button(root, text='Generate config file', command= lambda: generate_config(root, e1.get(), e2.get(), e3.get())).grid(row=4, column=0, sticky=tk.W, pady=4)
    tk.Button(root,text="Close", command= lambda: quit_win(root)).grid(row=4, column=1, sticky=tk.W, pady=4)

def add_labels(root):
    tk.Label(root, text="Source directory").grid(row=0)
    tk.Label(root, text="Destination directory").grid(row=1)
    tk.Label(root, text="File name").grid(row=2)

def generate_config(root, source_path, destination_path, file_name):
    cs.create_config_file(source_path, destination_path, file_name)
    quit_win(root)
    cts.run()

if __name__ == '__main__':
    present_user_config_form()
