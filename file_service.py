# -*- coding: utf-8 -*-

import os, time, datetime, shutil
from pathlib import Path

results = {0:'Copy/Rename operation: SUCCESS!!!',
           1:'File already exists!',
           2:'ERROR!!! Sth went wrong with copy or rename operation...',
           3:'File could not be found!!!'}

def get_creation_date(file_path):
    try:
        modified_date = time.ctime(os.path.getmtime(file_path))
    except OSError:
        modified_date = 0
    stripped_date = datetime.datetime.strptime(modified_date, "%a %b %d %H:%M:%S %Y")
    formatted_date = stripped_date.strftime("%y%m%d_%H%M%S")
    return str(formatted_date)
    
def get_results_status(file_path):
    with open(file_path, 'r') as file:
        lines=file.read()
        pass_count = lines.count('class="pass')
        fail_count = lines.count('class="fail')
    return "_P_"+str(pass_count)+"_F_"+str(fail_count)

def create_file_name(file_path):
    formatted_file_name = get_creation_date(file_path)+get_results_status(file_path)
    return formatted_file_name+'.html'

def copy_results_file_and_rename(source_path, destination_path, old_name, new_name):
    path_before_rename = Path(destination_path+old_name)
    path_after_rename = Path(destination_path+new_name)
    if path_after_rename.exists():
        return 1
    else:
        shutil.copyfile(source_path,destination_path+old_name)
        return rename_file(path_before_rename, path_after_rename)
    
def rename_file(old_path, new_path):
    if old_path.exists(): 
        os.rename(old_path, new_path)
    else:
        return 3
    if new_path.exists():
        return 0
    else:
        return 2
    
def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
