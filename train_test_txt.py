import os
import random
import re

# Path ke direktori dataset
dataset_dir = r'C:\Users\RAFA\Ubuntu\RGBX\RGBX_Semantic_Segmentation\datasets\NYUDepthv2\RGB'

# Rasio train dan test (sesuai dengan repository di GitHub)
train_ratio = 0.55
test_ratio = 0.45

# Daftar file dalam direktori dataset
file_list = os.listdir(dataset_dir)

# Randomize urutan file
random.shuffle(file_list)

# Jumlah data train dan test
num_train = int(len(file_list) * train_ratio)
num_test = len(file_list) - num_train

# Memisahkan file menjadi data train dan test
train_files = file_list[:num_train]
test_files = file_list[num_train:]

# Menulis file train.txt
with open('train.txt', 'w') as f_train:
    for file_name in train_files:
        file_name_without_ext = re.sub(r'\.[^.]+$', '', file_name)
        f_train.write(file_name_without_ext + '\n')

# Menulis file test.txt
with open('test.txt', 'w') as f_test:
    for file_name in test_files:
        file_name_without_ext = re.sub(r'\.[^.]+$', '', file_name)
        f_test.write(file_name_without_ext + '\n')

