import torch
import timm
import cv2
import numpy as np
import torchvision.transforms as transforms
model = timm.create_model('efficientnet_b0', pretrained=True, num_classes=2)
model.eval()
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.5], [0.5])
    ])

    image = transform(image).unsqueeze(0)
    return image
def predict_deepfake(image_path):
    image = preprocess_image(image_path)
    with torch.no_grad():
        output = model(image)

    prediction = torch.argmax(output, dim=1).item()
    return "Real" if prediction == 1 else "Fake"
image_path = "images/your_image.jpg"  # Replace with actual path
result = predict_deepfake(image_path)
print(f"Prediction: {result}")
