import os
import sys

directory = input("Enter folder with path: ") # Ex :"C:/Samples/Test"  # Change this to your directory
response = input("Are you sure? (yes/no): ").strip().lower()
if response == "yes" or response == "y":
    old_text = input("Enter old text: ")
    new_text = input("Enter new text: ")
    
    if os.path.isdir(directory):
        for subdir, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                content = content.replace(old_text, new_text)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
        input("Text replaced. Press Enter to exit...")                
    else:
        print("Directory/folder does not exist.")
else:
    print("User canceled.")
    

    
    


   
