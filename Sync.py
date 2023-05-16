import os

def delete_images(folder_path, ratio):
    # Get a list of all the files in the folder
    files = os.listdir(folder_path)
    # Sort the files in ascending order
    files.sort()
    
    # Keep every other file
    files_to_keep = files[::2]
    # Calculate the number of files to delete based on the ratio
    num_files_to_delete = int(len(files_to_keep) * ratio)
    
    # Loop through the list of files to delete
    for file_to_delete in files_to_keep[:num_files_to_delete]:
        # Construct the path to the file to delete
        file_path = os.path.join(folder_path, file_to_delete)
        # Delete the file
        os.remove(file_path)

folder_path = r'C:\Users\RAFA\Downloads\dataset\1\testcode\infrared'
ratio = 0.86  # delete 56% of the images

a = folder_path + r'\test'
print(a)

delete_images(folder_path, ratio)
