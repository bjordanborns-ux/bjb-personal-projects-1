from pathlib import Path
import shutil
import logging

## - - - File Catigorization
file_categories = {
    "images" : [".jpg",".jpeg",".png",".gif"],
    "documents" : [".pdf",".docx",".txt"],
    "code" : [".py",".m",".js"],
    "videos" : [".mp4", ".mov"],
    "spreadsheets" : [".xlsx",".csv"],
    "archives" : [".zip",".rar"],
    "other" : []
}

sorted_files = {
    "images" : [],
    "documents" : [],
    "code" : [],
    "videos" : [],
    "spreadsheets" : [],
    "archives" : [],
    "other" : []
}

## - - - File Discovery
# Gets path from user
def path_discovery():
    while True:
        folder = Path(input("Enter folder path: "))
        
        if folder.is_dir():
            print("Folder Exists!")
            return folder
        else:
            print("Folder not found. Try again")

# Scans file for list, gives count of files, and sorts into categories
def scan_folder(selected_folder):
    print(f"Scanning folder: {selected_folder}...")
    print("------------------------------------")
    file_count = 0
    for item in selected_folder.iterdir():
        if item.is_file():
            print(item.name,'|', item.suffix)
            file_count += 1
            return file_count
    print("------------------------------------")
    print(f'Total files found: {file_count}')

def sort_folder_ext(selected_folder, file_categories, sorted_files):
    for item in selected_folder.iterdir():
        if item.is_file():
            if item.suffix.lower() in file_categories["images"]:
                sorted_files["images"].append(item)  
            elif item.suffix.lower() in file_categories["documents"]:
                sorted_files["documents"].append(item)  
            elif item.suffix.lower() in file_categories["code"]:
                sorted_files["code"].append(item)       
            elif item.suffix.lower() in file_categories["videos"]:
                sorted_files["videos"].append(item)  
            elif item.suffix.lower() in file_categories["spreadsheets"]:
                sorted_files["spreadsheets"].append(item)  
            elif item.suffix.lower() in file_categories["archives"]:
                sorted_files["archives"].append(item)   
            else:
                sorted_files["other"].append(item)  

selected_folder = path_discovery()

print("------------------------------------")
folder_count = scan_folder(selected_folder)

sort_folder_ext(selected_folder, file_categories, sorted_files)

print("------------------------------------")
if len(sorted_files["images"]) > 0:
    print(f"Images | {sorted_files["images"]}")
if len(sorted_files["documents"]) > 0:
    print(f"Documents | {sorted_files["documents"]}")
if len(sorted_files["code"]) > 0:
    print(f"Code | {sorted_files["code"]}")
if len(sorted_files["videos"]) > 0:    
    print(f"Videos | {sorted_files["videos"]}")
if len(sorted_files["spreadsheets"]) > 0:   
    print(f"Spreadsheets | {sorted_files["spreadsheets"]}")
if len(sorted_files["archives"]) > 0:    
    print(f"Archives | {sorted_files["archives"]}")
if len(sorted_files["other"]) > 0:   
    print(f"Other | {sorted_files["other"]}")