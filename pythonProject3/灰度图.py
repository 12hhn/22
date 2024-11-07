import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
matplotlib.use('TkAgg')

image_path = "微信图片_20240714185735.png"
image = Image.open(image_path)
gray_image = image.convert("L")

# 将灰度图转换为数组
gray_array = np.array(gray_image)

# 初始化直方图数组（每个像素值范围为 0-255）
hist = [0] * 256

# 计算直方图
for pixel in gray_array.flatten():
    hist[pixel] += 1

# 初始化累计分布函数 (CDF) 数组
cdf = [0] * 256

# 计算累计直方图
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i - 1] + hist[i]

# 归一化 CDF
cdf_normalized = [float(c) / max(cdf) * max(hist) for c in cdf]

# 显示灰度图
plt.figure(figsize=(10, 5))

# 显示原灰度图
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

# 绘制累计直方图
plt.subplot(1, 2, 2)
plt.plot(cdf_normalized, color='b')
plt.bar(range(256), hist, color='r', alpha=0.6)
plt.xlim([0, 256])
plt.title('Cumulative Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Cumulative Frequency')
plt.legend(('CDF', 'Histogram'), loc='upper left')
plt.grid(True)
plt.show()
