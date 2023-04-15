import cv2
import numpy as np
import matplotlib.pyplot as plt

img_file = "img/WhiteCat.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    kernel = np.ones((5, 5), dtype=np.float64) / 25.
    kernel[0, :] = -1, -2, -3, -2, -1
    kernel[1, :] = -2, -4, -6, -4, -2
    kernel[2, :] = 0, 0, 0, 0, 0
    kernel[3, :] = 2, 4, 6, 4, 2
    kernel[4, :] = 1, 2, 3, 2, 1
    print(kernel)

    filtered_img = cv2.filter2D(img, -1, kernel)

    plt.subplot(2, 1, 1)
    plt.title("Original")
    plt.imshow(img, cmap='gray')

    plt.subplot(2, 1, 2)
    plt.title("Horizontal Edge")
    plt.imshow(filtered_img, cmap='gray')

    plt.subplots_adjust(hspace=0.5)

    plt.show()