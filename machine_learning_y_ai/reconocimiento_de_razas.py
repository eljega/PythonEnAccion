import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import torch
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import torchvision.models as models
import torch.nn as nn
from tkinter.font import Font

dataset_path = 'dataset/train_dogs'
dataset = ImageFolder(root=dataset_path)
class_names = [name.split('-', 1)[-1].replace('_', ' ') for name in dataset.classes]

def load_model():
    model = models.resnet18(pretrained=True)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, len(class_names))
    model.load_state_dict(torch.load('model_dog_breeds.pth', map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

def load_image():
    file_path = filedialog.askopenfilename()
    img = Image.open(file_path).convert('RGB')
    img_tk = ImageTk.PhotoImage(img.resize((500, 500)))
    panel.configure(image=img_tk)
    panel.image = img_tk
    predict(img)

def predict(img):
    img_transforms = transforms.Compose([
        transforms.Resize((500, 500)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img_tensor = img_transforms(img).unsqueeze(0)
    outputs = model(img_tensor)
    _, predicted = torch.max(outputs, 1)
    prediction = class_names[predicted[0]]
    label.configure(text=f"Prediction: {prediction}")

root = tk.Tk()
root.title("Dog Breed Classifier")
root.geometry("600x700")
myFont = Font(family="Helvetica", size=18, weight="bold")
panel = tk.Label(root)
panel = tk.Label(root)
panel.pack()
button = tk.Button(root, text="Load image", command=load_image)
button.pack()
label = tk.Label(root, text="Prediction: None", font=myFont)
label.pack()
root.mainloop()
