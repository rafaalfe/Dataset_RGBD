import cv2
import numpy as np

def infrared_depth_fusion(infrared_image, depth_map):
    # Konversi depth map menjadi citra grayscale
    depth_map_gray = cv2.cvtColor(depth_map, cv2.COLOR_BGR2GRAY)

    # Normalisasi depth map menjadi rentang 0-255
    depth_map_normalized = cv2.normalize(depth_map_gray, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Resize citra inframerah sesuai dengan depth map
    infrared_resized = cv2.resize(infrared_image, (depth_map.shape[1], depth_map.shape[0]))

    # Konversi citra inframerah menjadi citra grayscale
    infrared_gray = cv2.cvtColor(infrared_resized, cv2.COLOR_BGR2GRAY)

    # Menggabungkan citra infrared dan depth map
    fused_image = cv2.addWeighted(infrared_gray, 0.5, depth_map_normalized, 0.5, 0)

    return fused_image

# Baca citra inframerah dan depth map
infrared_image = cv2.imread('infrared_image.jpg')
depth_map = cv2.imread('depth_map.jpg')

# Panggil fungsi penggabungan infrared dan depth map
fused_image = infrared_depth_fusion(infrared_image, depth_map)

# Tampilkan citra hasil penggabungan
cv2.imshow('Fused Image', fused_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
