# -*- coding: utf-8 -*-

import os
from pathlib import Path
import file_service as fs
import re

config_file="C:\\Users\\"+os.getlogin()+"\\.copy_test_file_config"
config_path=Path(config_file)
separator="="
props={}

def config_file_exists():
    return config_path.exists()

def config_file_is_valid():
    reg=r"source_path=[A-Za-z]:\\([a-zA-Z0-9\-\_\\\ ]+)[\n]destination_path=[A-Za-z]:\\([a-zA-Z0-9\-\_\\\ ]+)[\n]file_name=[\w\-. ]+.html$"
    with open(config_path, 'r') as file:
        content = file.read()
        match = re.search(reg, content)
    return match

def read_properties():
    with open(config_path, 'r') as file:
        for line in file:
            if separator in line:
                name, value = line.split(separator, 1)
                props[name.strip()] = value.strip()
    return props
    
def create_config_file(source_path, destination_path, file_name):
    properties = "source_path="+source_path.replace("/","\\")+"\ndestination_path="+destination_path.replace("/","\\")+"\nfile_name="+file_name
    fs.write_to_file(config_path, properties)
    
def should_config_file_be_recreated():
    if config_file_exists() and config_file_is_valid():
        return False
    return True


#print(should_config_file_be_recreated())
#print(config_file_exists())
#if(config_file_is_valid()):
#    print(True)