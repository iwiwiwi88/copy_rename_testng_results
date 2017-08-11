# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog
import config_service as cs
import copy_test_results as cts
import re

def present_user_config_form():
    root=tk.Tk()
    root.title("Configure copy/rename script")
    root.geometry("550x100")
    add_grid(root)
    root.mainloop()
    
def quit_win(root):
    root.destroy()

def add_grid(root):
    add_labels(root)

    e1 = tk.Entry(width=50)
    e2 = tk.Entry(width=50)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    
    tk.Button(root, text="Browse", command= lambda: browse_file(e1)).grid(row=0, column=2)
    tk.Button(root, text="Browse", command= lambda: browse_folder(e2)).grid(row=1, column=2)
    
    tk.Button(root, text='Generate config file', command= lambda: generate_config(root, e1.get(), e2.get())).grid(row=3, column=0, sticky=tk.W, pady=4)
    tk.Button(root, text="Close", command= lambda: quit_win(root)).grid(row=3, column=1, sticky=tk.W, pady=4)

def add_labels(root):
    tk.Label(root, text="File to be copied").grid(row=0)
    tk.Label(root, text="Destination directory").grid(row=1)

def browse_file(entry):
    directory = filedialog.askopenfilename()
    entry.delete(0,tk.END)
    entry.insert(0,directory)
    
def browse_folder(entry):
    directory = filedialog.askdirectory()
    entry.delete(0,tk.END)
    entry.insert(0,directory)
    
def generate_config(root, source_path, destination_path):
    file_regex = '[\w\-. ]+.html$'
    file_name = re.match(file_regex, source_path)[0]
    no_file_name_source_path = re.sub(file_name,"",source_path)
    cs.create_config_file(no_file_name_source_path, destination_path, file_name)
    quit_win(root)
    cts.run()

if __name__ == '__main__':
    present_user_config_form()
