import os

dataset_path = r'C:\Users\RAFA\Downloads\dataset'
rgb_input_folder_path = dataset_path + r'\color'
depth_input_folder_path = dataset_path + r'\depth'
rgb_output_folder_path = dataset_path + r'\color'
depth_output_folder_path = dataset_path + r'\depth'
i = 0

def rename():

    for filename in os.listdir(rgb_input_folder_path):
        if filename.endswith(".png"): #jika file adalah file gambar PNG
            new_name = str(i) + ".png" #buat nama baru sesuai urutan
            os.rename(os.path.join(rgb_output_folder_path, filename), os.path.join(rgb_output_folder_path, new_name))
            i += 1

    for filename in os.listdir(depth_input_folder_path):
        if filename.endswith(".png"): #jika file adalah file gambar PNG
            new_name = str(i) + ".png" #buat nama baru sesuai urutan
            os.rename(os.path.join(depth_output_folder_path, filename), os.path.join(depth_output_folder_path, new_name))
            i += 1

    return
