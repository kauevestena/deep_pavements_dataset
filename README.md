# Deep Pavements Dataset

A comprehensive image dataset for pavement surface classification using semantic models. This dataset contains 5,000 high-quality images across 10 different pavement surface types, designed for computer vision and machine learning research.

## Dataset Overview

The Deep Pavements Dataset is specifically designed for training and evaluating machine learning models on pavement surface classification tasks. All images are sourced from Wikimedia Commons, Mapillary, and Flickr under CC-compatible licenses, ensuring legal compliance for research and commercial use.

### Dataset Statistics

- **Total Images**: 5,000
- **Number of Classes**: 10
- **Images per Class**: 500
- **Format**: Various image formats (PNG, JPG)
- **License**: CC Compatible licenses
- **Source**: Wikimedia Commons, Mapillary, Flickr

### Surface Classes

The dataset includes the following pavement surface types, compliant with OpenStreetMap (OSM) tagging standards:

1. **Asphalt** - Standard road asphalt surfaces
2. **Cobblestone** - Traditional cobblestone surfaces
3. **Compacted** - Compacted earth or gravel surfaces
4. **Concrete** - Concrete pavement surfaces  
5. **Concrete Plates** - Large concrete slabs
6. **Grass** - Grass-covered surfaces
7. **Gravel** - Loose gravel surfaces
8. **Ground** - Natural earth/dirt surfaces
9. **Paving Stones** - Interlocking paver blocks
10. **Sett** - Small cobblestones or granite blocks

For detailed information about these surface types, refer to the [OSM surface tag documentation](https://wiki.openstreetmap.org/wiki/Key:surface).

## Repository Structure

```
deep_pavements_dataset/
├── README.md              # Main documentation
├── LICENSE               # MIT License
├── classes.txt           # List of class names
├── CONTRIBUTING.md       # Contribution guidelines
├── dataset/              # Main dataset directory
│   ├── asphalt/         # 500 asphalt images
│   ├── concrete/        # 500 concrete images
│   ├── paving_stones/   # 500 paving stones images
│   └── ...              # Other surface type directories
├── examples/             # Usage examples and quick start
│   ├── README.md        # Comprehensive usage examples
│   └── quick_start.py   # Quick verification script
├── scripts/              # Utility and analysis scripts
│   ├── ABOUT.md         # Scripts documentation
│   ├── constants.py     # Dataset constants
│   ├── lib.py           # Utility functions
│   ├── copying.py       # Dataset copying utilities
│   ├── requirements.txt # Python dependencies
│   └── *.ipynb          # Analysis notebooks
└── analysis/             # Analysis results and reports
    ├── figures/         # Generated charts and visualizations
    ├── finetuned/       # Fine-tuned model results
    └── raw_reports/     # Raw analysis reports
```

## Getting Started

### Quick Verification

Run the quick start script to verify the dataset is properly set up:

```bash
python examples/quick_start.py
```

This will display dataset statistics and confirm everything is ready for use.

### Prerequisites

- Python 3.7+
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/kauevestena/deep_pavements_dataset.git
cd deep_pavements_dataset
```

2. Create and activate a virtual environment:
```bash
python -m venv dpd
source dpd/bin/activate  # On Windows: dpd\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r scripts/requirements.txt
```

## Usage

### Basic Usage

The dataset is organized with folder names as labels. Each subdirectory in the `dataset/` folder contains 500 images of the corresponding surface type.

```python
import os

# List all available classes
classes = os.listdir('dataset/')
print(f"Available classes: {classes}")

# Count images per class
for class_name in classes:
    count = len(os.listdir(f'dataset/{class_name}'))
    print(f"{class_name}: {count} images")
```

### Using the Utility Scripts

The repository includes several utility scripts for dataset management and analysis:

- **copying.py**: Copy and organize images from external sources
- **lib.py**: Core utility functions for dataset operations
- **Analysis notebooks**: Jupyter notebooks for model evaluation and visualization

See [scripts/ABOUT.md](scripts/ABOUT.md) for detailed documentation on using these tools.

### Code Examples

For comprehensive code examples including PyTorch and TensorFlow integration, see [examples/README.md](examples/README.md).

## Dataset Design Philosophy

### Collection Principles

- **Variety**: Images span all categories of quality and resolution to ensure model robustness
- **Minimal Effort**: No subcategories or fine-grained trait discrimination to keep the dataset simple and focused
- **Manual Curation**: While some classes are automatically generated, all are manually curated for quality
- **OSM Compliance**: All labels follow OpenStreetMap surface tagging standards for consistency

### Quality Considerations

- Images represent real-world conditions with varying lighting, angles, and quality
- No artificial preprocessing or enhancement to maintain authentic conditions
- Balanced dataset with equal representation across all classes
- Mixed resolution and quality to improve model generalization

## Analysis and Evaluation

The repository includes comprehensive analysis tools for model evaluation:

- **Model Comparison**: Tools for comparing different computer vision models
- **Performance Metrics**: Confusion matrices, classification reports, and accuracy metrics
- **Visualization**: Charts and plots for result analysis
- **Fine-tuning Results**: Evaluation of fine-tuned models on the dataset

## License and Citation

This dataset is released under the MIT License. All images are sourced from platforms with CC-compatible licenses.

### Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{deep_pavements_dataset,
  title={Deep Pavements Dataset},
  author={Kauê de Moraes Vestena},
  year={2024},
  url={https://github.com/kauevestena/deep_pavements_dataset},
  note={A comprehensive dataset for pavement surface classification}
}
```

## Contributing

Contributions to improve the dataset or analysis tools are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

For major changes, please open an issue first to discuss the proposed modifications.

## Related Projects

- [Deep Pavements Sample Picker](https://github.com/kauevestena/deep_pavements_sample_picker) - Tools for quality testing and sample selection

## Contact

For questions, issues, or collaboration opportunities, please open an issue on GitHub or contact the repository maintainer.
