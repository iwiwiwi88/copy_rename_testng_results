# -*- coding: utf-8 -*-

import tkinter as tk
import webbrowser as wb
import subprocess as sp
import file_service as fs

def present_results(cr_result, folder, file):
    root=tk.Tk()
    root.title("Copy/Rename Tool")
    root.geometry("600x200")
    add_labels(root, cr_result, folder, file)
    add_buttons(root, folder, file)
    root.mainloop()
    
def add_labels(root, cr_result, folder, file):
    add_main_text(root, folder, file)
    add_result_label(root, cr_result)
    
def add_main_text(root, folder, file):
    text = tk.Text(root, height=2, font="Helvetica 14", )
    text.tag_configure("bold", font="Helvetica 14 bold", justify="center")
    text.tag_configure("center", justify='center')
    text.insert("end", "Copy/Rename of file to folder: "+folder+"\n", "center") 
    text.insert("end", file, "bold") 
    text.configure(state="disabled")
    text.pack()
    
def add_result_label(root, cr_result):
    if cr_result==0:
        tk.Label(root, text=fs.results[cr_result], fg = "light green", bg = "dark green",
		 font = "Helvetica 14 bold").pack()
    elif cr_result==1:
        tk.Label(root, text=fs.results[cr_result], fg = "blue", bg = "yellow",
		 font = "Helvetica 14 bold").pack()
    else:
        tk.Label(root, text=fs.results[cr_result], fg = "orange", bg = "red",
		 font = "Helvetica 14 bold").pack()
    
def add_buttons(root, folder, file):
    tk.Button(root,text="Open in browser", command= lambda: open_in_browser(folder+file, root)).pack()
    tk.Button(root,text="Open folder", command= lambda: open_folder(folder,root)).pack()
    tk.Button(root,text="Close", command= lambda: quit_win(root)).pack()
    
def open_in_browser(path, root):
    url = path
    wb.open(url,new=2)
    quit_win(root)
    
def open_folder(folder, root):
    sp.Popen(r'explorer '+folder)
    quit_win(root)
    
def quit_win(root):
    root.destroy()
    