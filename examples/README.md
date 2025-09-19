# Usage Examples

This directory contains practical examples of how to use the Deep Pavements Dataset for various machine learning and computer vision tasks.

## Basic Dataset Operations

### Loading the Dataset

```python
import os
import numpy as np
from PIL import Image
import pandas as pd

def load_dataset(dataset_path='dataset/', image_size=(224, 224)):
    """
    Load the complete dataset with labels.
    
    Args:
        dataset_path: Path to the dataset directory
        image_size: Tuple of (width, height) for image resizing
    
    Returns:
        images: List of PIL Images
        labels: List of corresponding labels
        class_names: List of unique class names
    """
    images = []
    labels = []
    class_names = sorted(os.listdir(dataset_path))
    
    for class_idx, class_name in enumerate(class_names):
        class_path = os.path.join(dataset_path, class_name)
        if not os.path.isdir(class_path):
            continue
            
        for image_file in os.listdir(class_path):
            if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(class_path, image_file)
                try:
                    image = Image.open(image_path).convert('RGB')
                    if image_size:
                        image = image.resize(image_size)
                    images.append(image)
                    labels.append(class_idx)
                except Exception as e:
                    print(f"Error loading {image_path}: {e}")
    
    return images, labels, class_names

# Example usage
images, labels, class_names = load_dataset()
print(f"Loaded {len(images)} images across {len(class_names)} classes")
print(f"Classes: {class_names}")
```

### Dataset Statistics

```python
def analyze_dataset(dataset_path='dataset/'):
    """Generate comprehensive dataset statistics."""
    stats = {}
    total_images = 0
    
    for class_name in sorted(os.listdir(dataset_path)):
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            count = len([f for f in os.listdir(class_path) 
                        if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
            stats[class_name] = count
            total_images += count
    
    print(f"Dataset Statistics:")
    print(f"Total Images: {total_images}")
    print(f"Number of Classes: {len(stats)}")
    print(f"\nPer-class Distribution:")
    for class_name, count in stats.items():
        percentage = (count / total_images) * 100
        print(f"  {class_name}: {count} images ({percentage:.1f}%)")
    
    return stats

# Example usage
stats = analyze_dataset()
```

## Machine Learning Integration

### PyTorch DataLoader

```python
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os

class PavementDataset(Dataset):
    """PyTorch Dataset for Deep Pavements Dataset."""
    
    def __init__(self, dataset_path='dataset/', transform=None, split='train', split_ratio=0.8):
        self.dataset_path = dataset_path
        self.transform = transform
        self.images = []
        self.labels = []
        self.class_names = sorted(os.listdir(dataset_path))
        self.class_to_idx = {name: idx for idx, name in enumerate(self.class_names)}
        
        # Load all image paths and labels
        for class_name in self.class_names:
            class_path = os.path.join(dataset_path, class_name)
            if os.path.isdir(class_path):
                class_images = [f for f in os.listdir(class_path) 
                              if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                
                # Split into train/test
                split_idx = int(len(class_images) * split_ratio)
                if split == 'train':
                    selected_images = class_images[:split_idx]
                else:
                    selected_images = class_images[split_idx:]
                
                for img_file in selected_images:
                    self.images.append(os.path.join(class_path, img_file))
                    self.labels.append(self.class_to_idx[class_name])
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        image_path = self.images[idx]
        label = self.labels[idx]
        
        image = Image.open(image_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
        
        return image, label

# Data transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                        std=[0.229, 0.224, 0.225])
])

# Create datasets
train_dataset = PavementDataset(transform=transform, split='train')
test_dataset = PavementDataset(transform=transform, split='test')

# Create data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

print(f"Training samples: {len(train_dataset)}")
print(f"Testing samples: {len(test_dataset)}")
print(f"Classes: {train_dataset.class_names}")
```

## Quick Start Example

For a complete working example, save this as `quick_start.py`:

```python
#!/usr/bin/env python3
"""
Quick start example for Deep Pavements Dataset
Usage: python quick_start.py
"""

import os
import sys
import matplotlib.pyplot as plt
from collections import Counter

def main():
    dataset_path = 'dataset/'
    
    if not os.path.exists(dataset_path):
        print("Error: Dataset directory not found. Please ensure you're in the repository root.")
        sys.exit(1)
    
    print("=== Deep Pavements Dataset Quick Start ===\n")
    
    # Analyze dataset
    print("1. Dataset Analysis:")
    class_counts = {}
    total_images = 0
    
    for class_name in sorted(os.listdir(dataset_path)):
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            count = len([f for f in os.listdir(class_path) 
                        if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
            class_counts[class_name] = count
            total_images += count
    
    print(f"   Total Images: {total_images}")
    print(f"   Number of Classes: {len(class_counts)}")
    print(f"   Classes: {list(class_counts.keys())}")
    
    print("\n2. Class Distribution:")
    for class_name, count in class_counts.items():
        print(f"   {class_name:15s}: {count:3d} images")
    
    print("\n3. Dataset is ready for use!")
    print("   - Use the examples in this directory for ML integration")
    print("   - Check scripts/ABOUT.md for analysis tools")
    print("   - See README.md for comprehensive documentation")

if __name__ == "__main__":
    main()
```

## Next Steps

1. **Basic Usage**: Run `python examples/quick_start.py` to verify dataset access
2. **Machine Learning**: Use the PyTorch or TensorFlow examples above
3. **Analysis**: Explore the Jupyter notebooks in the `scripts/` directory
4. **Custom Models**: Adapt the dataset loading code for your specific needs

For more detailed examples and advanced usage, see the individual script files and notebooks in the `scripts/` directory.