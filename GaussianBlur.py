import cv2
import matplotlib.pyplot as plt

img_file = "img/WhiteCat.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    gausian_img1 = cv2.GaussianBlur(img, (0, 0), 1)
    gausian_img2 = cv2.GaussianBlur(img, (0, 0), 3)
    gausian_img3 = cv2.GaussianBlur(img, (0, 0), 5)

    plt.subplot(2, 2, 1)
    plt.title("Original")
    plt.imshow(img, cmap='gray')

    plt.subplot(2, 2, 2)
    plt.title("Sigma = 1")
    plt.imshow(gausian_img1, cmap='gray')

    plt.subplot(2, 2, 3)
    plt.title("Sigma = 3")
    plt.imshow(gausian_img2, cmap='gray')

    plt.subplot(2, 2, 4)
    plt.title("Sigma = 5")
    plt.imshow(gausian_img3, cmap='gray')

    plt.show()