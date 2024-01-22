from PIL import Image
Image.open('Apple.jpg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('Apple.jpg')
w , h,d =tuple(img.shape)
pixels = np.reshape(img, (w*h , d))
from sklearn.cluster import KMeans

n_colors = 10
models = KMeans(n_clusters=n_colors, random_state=42).fit(pixels)
palette = np.uint8(models.cluster_centers_)
plt.imshow([palette])
plt.show()