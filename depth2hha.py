import cv2
import numpy as np

def convert_image_to_hha(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the horizontal disparity
    horizontal_disparity = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)

    # Calculate the height above ground
    height_above_ground = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)

    # Calculate the angle
    angle = cv2.phase(horizontal_disparity, height_above_ground, angleInDegrees=True)

    # Normalize the values
    horizontal_disparity = cv2.normalize(horizontal_disparity, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    height_above_ground = cv2.normalize(height_above_ground, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    angle = cv2.normalize(angle, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Stack the HHA channels
    hha_image = np.stack((horizontal_disparity, height_above_ground, angle), axis=2)

    return hha_image

# Path to the input image
input_image_path = r"C:\Users\RAFA\source\repos\Depth2HHA-python\demo\0.png"

# Convert the image to HHA representation
hha_image = convert_image_to_hha(input_image_path)

# Save the HHA image
cv2.imwrite(r"C:\Users\RAFA\source\repos\Depth2HHA-python\demo\0_HHA.png", hha_image)
