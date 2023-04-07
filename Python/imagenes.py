import numpy as np
import cv2
import matplotlib.pyplot as plt

# leemos la imagen con tipo nparray
image = cv2.imread('imagenes/ganado sano grises/2.2.png')

# si la queremos mostrar
plt.imshow(image)
plt.show()

# para recortarla

a = image[100:, 200:, :]
plt.imshow(a)
plt.imshow(image)

#crear una imagen
img = np.zeros((200, 300), np.uint8)
img2 = np.ones((200, 300), np.uint8)