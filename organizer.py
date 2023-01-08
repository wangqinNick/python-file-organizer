import os
import shutil

def organize_files(directory):
    # Create a dictionary to map file types to subdirectories
    file_types = {}

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Ignore hidden files
        if filename.startswith('.'):
            continue

        # Get the file extension
        file_extension = filename.split('.')[-1]

        # If the file extension is not a key in the dictionary, add it
        # and create a new subdirectory for it
        if file_extension not in file_types:
            file_types[file_extension] = file_extension + '_files'
            os.makedirs(os.path.join(directory, file_types[file_extension]))

        # Move the file to the appropriate subdirectory
        shutil.move(os.path.join(directory, filename), 
                    os.path.join(directory, file_types[file_extension], filename))

# Test the function
organize_files('/Users/qinwang/desktop/')
print("Heo")
