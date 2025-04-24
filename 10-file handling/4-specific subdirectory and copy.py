import os
import shutil

source_file_path = ""     #existing path     
destination_dir = ""       #new path

os.makedirs(destination_dir, exist_ok=True)

shutil.copy(source_file_path, destination_dir)

print("File copied from source path to destination path")
