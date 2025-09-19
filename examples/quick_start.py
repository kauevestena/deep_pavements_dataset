#!/usr/bin/env python3
"""
Quick start example for Deep Pavements Dataset
Usage: python examples/quick_start.py
"""

import os
import sys
from collections import Counter

def main():
    # Look for dataset in the repository root
    possible_paths = ['dataset/', '../dataset/']
    dataset_path = None
    
    for path in possible_paths:
        if os.path.exists(path):
            dataset_path = path
            break
    
    if not dataset_path:
        print("Error: Dataset directory not found.")
        print("Please ensure you're running this script from the repository root or examples directory.")
        sys.exit(1)
    
    print("=== Deep Pavements Dataset Quick Start ===\n")
    
    # Analyze dataset
    print("1. Dataset Analysis:")
    class_counts = {}
    total_images = 0
    
    for class_name in sorted(os.listdir(dataset_path)):
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            # Count image files
            image_files = [f for f in os.listdir(class_path) 
                          if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            count = len(image_files)
            class_counts[class_name] = count
            total_images += count
    
    print(f"   Total Images: {total_images}")
    print(f"   Number of Classes: {len(class_counts)}")
    print(f"   Average per class: {total_images // len(class_counts) if class_counts else 0}")
    
    print("\n2. Class Distribution:")
    for class_name, count in class_counts.items():
        percentage = (count / total_images * 100) if total_images > 0 else 0
        print(f"   {class_name:15s}: {count:3d} images ({percentage:5.1f}%)")
    
    # Check for balanced dataset
    if class_counts:
        counts = list(class_counts.values())
        is_balanced = all(c == counts[0] for c in counts)
        print(f"\n3. Dataset Balance: {'✓ Balanced' if is_balanced else '✗ Imbalanced'}")
        
        if not is_balanced:
            print(f"   Min: {min(counts)} images")
            print(f"   Max: {max(counts)} images")
    
    print("\n4. Sample File Check:")
    if class_counts:
        first_class = next(iter(class_counts.keys()))
        first_class_path = os.path.join(dataset_path, first_class)
        sample_files = [f for f in os.listdir(first_class_path)[:3] 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        print(f"   Sample files from '{first_class}':")
        for sample in sample_files:
            print(f"     - {sample}")
    
    print("\n5. Next Steps:")
    print("   ✓ Dataset is ready for use!")
    print("   → Use examples in this directory for ML integration")
    print("   → Check scripts/ABOUT.md for analysis tools")
    print("   → See README.md for comprehensive documentation")
    print("   → Try: python -c \"from scripts.lib import get_sample_amounts; get_sample_amounts()\"")

if __name__ == "__main__":
    main()