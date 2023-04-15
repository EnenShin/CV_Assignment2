import cv2
import matplotlib.pyplot as plt

img_file = "img/WhiteCat.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    filtered_img = cv2.boxFilter(img, -1, (5, 5))

    plt.subplot(2, 1, 1)
    plt.title("Original")
    plt.imshow(img, cmap='gray')

    plt.subplot(2, 1, 2)
    plt.title("Average Filter")
    plt.imshow(filtered_img, cmap='gray')

    plt.subplots_adjust(hspace=0.5)

    plt.show()