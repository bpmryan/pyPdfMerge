import PyPDF2
import os

# pip install PyPDF2
merger = PyPDF2.PdfMerger()

# reads the current working directory (cwd) 
for filename in os.listdir(os.getcwd()) :
    if filename.endswith('.pdf') :
        merger.append(filename)

merger.write("merged.pdf")
merger.close()
# check if the merged file is created
print("PDFs merged successfully into 'merged.pdf'")