import os

print("🔍 Checking if script is running...")

img_path = "images/your_image.jpg"

if os.path.exists(img_path):
    print("✅ Image found!")
else:
    print("❌ Image NOT found!")
