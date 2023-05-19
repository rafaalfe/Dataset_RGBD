import numpy as np
import cv2

def fill_holes_depth_map(depth_map):
    # Menggunakan algoritma pengisian lubang di OpenCV
    hole_filled = cv2.inpaint(depth_map, (depth_map == 0).astype(np.uint8), 3, cv2.INPAINT_TELEA)
    return hole_filled

# Contoh penggunaan program

# Membaca gambar depth map
depth_image = cv2.imread(r"C:\Users\RAFA\source\repos\Depth2HHA-python\demo\51.png", cv2.IMREAD_GRAYSCALE)

    # Convert the image to grayscale
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Memanggil fungsi untuk mengisi lubang
filled_image = fill_holes_depth_map(depth_image)

# Menampilkan gambar depth map asli
cv2.imshow('Depth Map', depth_image)
cv2.waitKey(0)

# Menampilkan gambar depth map setelah lubang diisi
cv2.imshow('Filled Depth Map', filled_image)
cv2.waitKey(0)

# Menyimpan gambar depth map setelah lubang diisi
cv2.imwrite(r"C:\Users\RAFA\source\repos\Depth2HHA-python\demo\51_filled.png", filled_image)

# Menutup semua jendela tampilan
cv2.destroyAllWindows()
