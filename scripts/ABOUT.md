# Scripts and Analysis Tools

This directory contains utility scripts and analysis tools for working with the Deep Pavements Dataset. These tools help with dataset management, model evaluation, and result visualization.

## Directory Contents

### Core Scripts

- **`constants.py`** - Dataset constants and configuration
- **`lib.py`** - Core utility functions for dataset operations
- **`copying.py`** - Dataset copying and organization utilities
- **`requirements.txt`** - Python package dependencies

### Analysis Notebooks

- **`charts_generation.ipynb`** - Generate comparison charts for multiple models
- **`charts_finetuned.ipynb`** - Analysis of fine-tuned model performance
- **`charts_finetuned_single.ipynb`** - Single model fine-tuning analysis

## Getting Started

### Environment Setup

1. Create a virtual environment:
```bash
python -m venv dpd
# On Linux/Mac:
source dpd/bin/activate
# On Windows:
dpd\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r scripts/requirements.txt
```

### Dependencies

The scripts require the following Python packages:
- **pandas** - Data manipulation and analysis
- **plotly** - Interactive visualizations
- **scikit-learn** - Machine learning metrics and tools
- **jupyter** - Notebook environment
- **ipykernel** - Jupyter kernel support
- **nbformat** - Notebook format handling
- **matplotlib** - Additional plotting capabilities

## Script Usage

### copying.py

Utility script for copying and organizing images from external sources into the dataset structure.

**Usage:**
```bash
python scripts/copying.py --input /path/to/source/folder
```

**Parameters:**
- `--input`: Path to input folder containing subfolders named after standard classes

**Functionality:**
- Copies files from input folder to the `dataset/` directory
- Generates unique filenames using MD5 hashing to prevent conflicts
- Creates class folders automatically based on input structure
- Maintains original file extensions

**Example:**
```bash
# Copy images from a new collection
python scripts/copying.py --input ./new_pavement_images/
```

### lib.py

Core library containing utility functions used across multiple scripts.

**Key Functions:**

- `create_folder(path)` - Create directory if it doesn't exist
- `get_path_last_part(path)` - Extract the last part of a file path
- `get_unique_filename(foldername, filename)` - Generate MD5-based unique filename
- `read_raw_reports(inpath)` - Read and process analysis reports
- `get_sample_amounts()` - Count samples per class
- `get_avaliable_classes_alphabetic()` - Get sorted list of available classes
- `read_json(path)` - JSON file reader

### Analysis Notebooks

#### charts_generation.ipynb

Generates comprehensive comparison charts for multiple computer vision models tested on the dataset.

**Features:**
- Model performance comparison
- Confusion matrix visualization
- Classification report analysis
- Support for multiple model architectures (ViT, ResNet, CLIP variants)

**Output:** 
- Interactive plots comparing model accuracy
- Detailed performance metrics
- Exportable charts for publications

#### charts_finetuned.ipynb

Analyzes the performance of fine-tuned models on the dataset.

**Features:**
- Fine-tuning results evaluation
- Comparison with baseline models
- Performance improvement analysis
- Statistical significance testing

#### charts_finetuned_single.ipynb

Focused analysis of individual fine-tuned model performance.

**Features:**
- Single model deep-dive analysis
- Class-wise performance breakdown
- Error analysis and misclassification patterns

## Analysis Pipeline

### Prerequisites for Analysis

The analysis notebooks require pre-computed model evaluation reports. These reports must be generated using the [sample picker repository](https://github.com/kauevestena/deep_pavements_sample_picker/blob/main/quality_tests/test_surface_samples.py) which contains CUDA-dependent libraries for model inference.

### Workflow

1. **Generate Reports**: Use the sample picker repository to evaluate models and generate CSV reports
2. **Place Reports**: Copy generated reports to `analysis/raw_reports/` directory
3. **Run Analysis**: Execute the Jupyter notebooks to generate visualizations and metrics
4. **Export Results**: Save charts and metrics to `analysis/figures/`

### Report Structure

Analysis reports should be CSV files with the following structure:
- Image filename as index
- Prediction confidence scores for each class
- Ground truth labels
- Model predictions

## Working with VSCode

For an integrated development experience:

1. Install the Python extension for VSCode
2. Open the repository folder in VSCode
3. Select the virtual environment as the Python interpreter
4. Use the built-in Jupyter notebook support for analysis

## Troubleshooting

### Common Issues

**ModuleNotFoundError**: Ensure all dependencies are installed in your virtual environment:
```bash
pip install -r scripts/requirements.txt
```

**Empty Analysis Reports**: Verify that model evaluation reports are present in `analysis/raw_reports/`

**Permission Errors**: Ensure write permissions for the `analysis/figures/` directory

### Performance Notes

- Large datasets may require significant memory for analysis
- Model evaluation (not included in this repository) requires CUDA-compatible hardware
- Notebook execution time varies based on dataset size and analysis complexity

## Contributing

When adding new scripts or analysis tools:

1. Follow the existing code structure and naming conventions
2. Add appropriate documentation and comments
3. Update this README with new functionality
4. Include example usage and expected outputs
5. Add any new dependencies to `requirements.txt`