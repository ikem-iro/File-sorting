import os
import shutil



def sort_folders():
    """
    The function `sort_folders` takes user input for a directory name, creates the directory if it
    doesn't exist, sorts files based on their extensions, and moves them to corresponding
    subdirectories.
    """
    directory_name = input("Enter the name of the directory you wish to go to:\n")

    directory_path = f'/Enter/your/path/here/{directory_name}'

    try:
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        os.chdir(directory_path)


        for file in os.listdir():
            if not os.path.exists(file):
                raise FileNotFoundError("No files in this directory")
            if os.path.isdir(file):
                continue
            if file.startswith('.'):
                continue
            _, file_extension =  os.path.splitext(file)
            file_extension = file_extension.split('.')[-1]
            if file_extension == '':
                os.mkdir("no extension")
                shutil.move(file, "no extension")
            if file.endswith(file_extension):
                if not os.path.isdir(f"{file_extension}_files"):
                    os.mkdir(f"{file_extension}_files")
                shutil.move(file, f"{file_extension}_files")
                if os.path.exists(file):
                    raise FileExistsError("File already exists in this directory")
                print("\nFiles have  been sorted and moved successfully.")
            
    except (FileNotFoundError, FileExistsError) as e:
        print(f"{e}")
            

sort_folders()