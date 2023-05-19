import os
from PIL import Image

def convert_images(input_folder, output_folder):
    # Membuat folder output ppm jika belum ada
    output_ppm_folder = os.path.join(output_folder, 'ppm')
    if not os.path.exists(output_ppm_folder):
        os.makedirs(output_ppm_folder)

    # Membuat folder output pgm jika belum ada
    output_pgm_folder = os.path.join(output_folder, 'pgm')
    if not os.path.exists(output_pgm_folder):
        os.makedirs(output_pgm_folder)

    # Mendapatkan daftar file di folder input
    file_list = os.listdir(input_folder)

    for file_name in file_list:
        # Memisahkan nama file dan ekstensi
        base_name, extension = os.path.splitext(file_name)

        # Mengabaikan file selain .ppm dan .pgm
        if extension.lower() not in ['.ppm', '.pgm']:
            continue

        # Membaca gambar menggunakan PIL
        image_path = os.path.join(input_folder, file_name)
        image = Image.open(image_path)

        # Mengubah format gambar ke PNG
        png_file = base_name + '.png'

        if extension.lower() == '.ppm':
            output_path = os.path.join(output_ppm_folder, png_file)
        else:  # extension.lower() == '.pgm'
            output_path = os.path.join(output_pgm_folder, png_file)

        image.save(output_path, 'PNG')

        print(f"File {file_name} berhasil dikonversi ke PNG.")

    print("Konversi selesai!")

# Menggunakan folder input dan output sesuai kebutuhan
input_folder = r'K:\Mentah\study_rooms\study_room_0001'
output_folder = r'K:\Mentah\study_rooms\converted'

# Memanggil fungsi untuk mengonversi gambar
convert_images(input_folder, output_folder)
