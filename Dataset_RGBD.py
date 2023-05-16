from asyncio import subprocess
import os
from pickle import TRUE
import sys
from turtle import width
from PIL import Image

dataset_path = r'C:\Users\RAFA\Downloads\dataset'

# Input and output folder paths
input_folder = r'C:\Users\RAFA\Downloads\dataset'
rgb_output_folder = dataset_path + r'\color'

# Buat folder output jika tidak ada
if not os.path.exists(rgb_output_folder):
    os.makedirs(rgb_output_folder)

def raw2png():
    # Define constants
    WIDTH = 640
    HEIGHT = 480
    YUYV_BYTES_PER_PIXEL = 2
    RGBA_BYTES_PER_PIXEL = 4

    # Loop through all files in input folder
    for filename in os.listdir(input_folder):
        # Check if file is a raw file
        if filename.endswith('.raw'):
            # Open .raw file with YUYV pixel format
            with open(os.path.join(input_folder, filename), 'rb') as f:
                data = f.read()

            # Convert YUYV data to RGBA data
            rgba_data = bytearray(WIDTH * HEIGHT * RGBA_BYTES_PER_PIXEL)
            for i in range(0, WIDTH * HEIGHT * YUYV_BYTES_PER_PIXEL, YUYV_BYTES_PER_PIXEL * 2):
                y0 = data[i]
                u = data[i + 1] - 128
                y1 = data[i + 2]
                v = data[i + 3] - 128

                r = int(max(0, min(255, y0 + 1.402 * v)))
                g = int(max(0, min(255, y0 - 0.344 * u - 0.714 * v)))
                b = int(max(0, min(255, y0 + 1.772 * u)))

                rgba_data[i * 2] = r
                rgba_data[i * 2 + 1] = g
                rgba_data[i * 2 + 2] = b
                rgba_data[i * 2 + 3] = 255

                r = int(max(0, min(255, y1 + 1.402 * v)))
                g = int(max(0, min(255, y1 - 0.344 * u - 0.714 * v)))
                b = int(max(0, min(255, y1 + 1.772 * u)))

                rgba_data[i * 2 + 4] = r
                rgba_data[i * 2 + 5] = g
                rgba_data[i * 2 + 6] = b
                rgba_data[i * 2 + 7] = 255

            # Create Image object and save as .png
            output_filename = os.path.splitext(filename)[0] + '.png'
            output_path = os.path.join(rgb_output_folder, output_filename)
            img = Image.frombytes('RGBA', (WIDTH, HEIGHT), bytes(rgba_data))
            img.save(output_path, 'PNG')
    return