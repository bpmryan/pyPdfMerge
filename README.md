# pyPdfMerge
Attempt on learning how to use Python and solve one my own issues

## Current Issue(s)
- Have to find a shady website, signup, upload files (potentially steal data), and merge files
- Doesn't have a function to upload a pdf link / physical pdf into terminal and merge (has to be done in IDE)

## Influence 
[@Cod1ngTogether](https://www.youtube.com/@Cod1ngTogether/shorts) \
- Video : [PDF Merger - Python for Beginners](https://youtube.com/shorts/nbytJbFli9s?si=JCVstypT2_sBjyiQ)

## Inital Code by Cod1ngTogether
```
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
```

## Upgrades (Future Plans)
- Function that allows the user to add pdfs instead of downloading an IDE, this script, and upload the pdfs into the IDE to merge 2 pdfs
- Have a cap of 10 pdfs that a user can merge
- Eventually create and deploy a website version instead of terminal 
- **In Short :** needs to be more accessible in terminal rather than through IDE