import os
import shutil

folder_path = input("Enter folder path: ")

files = os.listdir(folder_path)

for file in files:
    full_path = os.path.join(folder_path, file)

    if os.path.isfile(full_path):

        extension = file.split(".")[-1].lower()

        if extension in ["jpg", "png", "jpeg"]:
            target_folder = "Images"

        elif extension in ["pdf", "docx", "txt"]:
            target_folder = "Documents"

        elif extension in ["mp4", "mkv"]:
            target_folder = "Videos"

        elif extension in ["py", "cpp", "java"]:
            target_folder = "Code"

        else:
            target_folder = "Others"

        new_folder_path = os.path.join(folder_path, target_folder)

        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)

        shutil.move(full_path, os.path.join(new_folder_path, file))

print("Files Organized Successfully!")