import os
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader

# Define Dataset Paths
real_path = "/Users/atmadipbakshi/Downloads/FaceForensics-master/dataset/DeepFakeDetection"
fake_path = "/Users/atmadipbakshi/Downloads/FaceForensics-master/dataset/DeepFakes"

# Image Transformations
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

# Load Dataset
dataset = datasets.ImageFolder(root="/Users/atmadipbakshi/Downloads/FaceForensics-master/dataset/",
                               transform=transform)

dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

# Define a Simple CNN Model
class DeepFakeCNN(nn.Module):
    def __init__(self):
        super(DeepFakeCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(64 * 32 * 32, 128)
        self.fc2 = nn.Linear(128, 2)  # 2 classes (real, fake)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = x.view(x.size(0), -1)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Initialize Model, Loss & Optimizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = DeepFakeCNN().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training Loop
for epoch in range(10):  # 10 epochs
    for images, labels in dataloader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")
