import cv2
import numpy as np
import torch
from torchvision import transforms
import os

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.imread(image_path)
    image = cv2.resize(image, (224, 224))

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])

    return transform(image).unsqueeze(0)


if __name__ == "__main__":
    img_path = "images/your_image.jpg"  
    img_tensor = preprocess_image(img_path)
    print("Tensor shape:", img_tensor.shape)
