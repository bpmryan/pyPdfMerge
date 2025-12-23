import PyPDF2
import os

# pip install PyPDF2
merger = PyPDF2.PdfMerger()

# user is prompted to upload their pdf files to be merged 
# find a way for the user to be forced to open their file explorer to select files


# reads the current working directory (cwd) 
for filename in os.listdir(os.getcwd()) :
    if filename.endswith('.pdf') :
        merger.append(filename)

# function to prompt user to confirm if they want to merge the files
# def user_files() :
#     # prompt user to upload files
#     file_path = input("Please enter the full path to your file: ").strip()
#     if os.path.exists(file_path) and os.path.isfile(file_path) :
#         print("Selected file\(s\): {file_path}")
#         return file_path
#     else : 
#         print(f"Error: The path `{file_path}` does not exist or is not a file. Please try again.")

# file_to_merge = user_files()

merger.write("merged.pdf")
merger.close()
# check if the merged file is created
print("PDFs merged successfully into 'merged.pdf'")