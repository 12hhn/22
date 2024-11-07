import cv2
import numpy as np

def image_fusion(img1_path, img2_path, alpha=0.5):
    # 读取图像
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # 检查图像是否成功读取
    if img1 is None:
        print(f"无法读取图像: {img1_path}")
        return
    if img2 is None:
        print(f"无法读取图像: {img2_path}")
        return

    # 确保两张图像的尺寸相同
    if img1.shape != img2.shape:
        print("图像尺寸不一致，请确保两张图像大小相同。")
        return

    # 图像融合
    fused_image = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

    # 显示结果
    cv2.imshow("Fused Image", fused_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 图像路径
img1_path = r'C:\照片1.jpg'
img2_path = r'C:\照片2.jpg'

# 调用图像融合函数
image_fusion(img1_path, img2_path, alpha=0.5)
