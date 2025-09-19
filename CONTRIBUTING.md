# Contributing to Deep Pavements Dataset

We welcome contributions to improve the Deep Pavements Dataset! This document provides guidelines for contributing to the project.

## Ways to Contribute

### 1. Dataset Improvements
- **Quality Control**: Report issues with image quality or labeling
- **New Images**: Contribute additional high-quality pavement images
- **Class Balance**: Help maintain balanced representation across classes
- **Metadata Enhancement**: Improve image metadata and documentation

### 2. Analysis Tools
- **New Analysis Scripts**: Add tools for dataset analysis and visualization
- **Model Evaluation**: Contribute evaluation scripts for new model architectures
- **Performance Metrics**: Implement additional evaluation metrics
- **Visualization**: Create new charts and visualization tools

### 3. Documentation
- **README Updates**: Improve main documentation
- **Script Documentation**: Document new or existing scripts
- **Usage Examples**: Add practical usage examples
- **Academic References**: Contribute relevant research references

### 4. Code Quality
- **Bug Fixes**: Report and fix issues in existing scripts
- **Code Optimization**: Improve script performance and efficiency
- **Testing**: Add unit tests for utility functions
- **Code Style**: Ensure consistent coding standards

## Getting Started

1. **Fork the Repository**
   ```bash
   # Fork via GitHub UI, then clone your fork
   git clone https://github.com/YOUR_USERNAME/deep_pavements_dataset.git
   cd deep_pavements_dataset
   ```

2. **Set Up Development Environment**
   ```bash
   python -m venv dpd
   source dpd/bin/activate  # On Windows: dpd\Scripts\activate
   pip install -r scripts/requirements.txt
   ```

3. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contribution Guidelines

### Code Standards

- **Python Style**: Follow PEP 8 guidelines
- **Documentation**: Document all functions and classes
- **Comments**: Use clear, descriptive comments
- **Naming**: Use descriptive variable and function names

### Dataset Contributions

#### Image Quality Standards
- **Resolution**: Minimum 224x224 pixels recommended
- **Format**: JPEG or PNG formats preferred
- **Quality**: Clear, well-lit images without excessive noise
- **Content**: Images should clearly show the pavement surface type
- **Licensing**: Only submit images with CC-compatible licenses

#### Image Organization
- Place images in appropriate class folders under `dataset/`
- Use the `copying.py` script for proper filename generation
- Verify class assignments match OSM surface standards
- Maintain balanced distribution across classes

### Script Contributions

#### New Scripts
- Add comprehensive docstrings
- Include usage examples in comments
- Add error handling for common issues
- Update `requirements.txt` if new dependencies are needed
- Document the script in `scripts/ABOUT.md`

#### Analysis Notebooks
- Clear markdown explanations for each step
- Meaningful variable names and comments
- Proper visualization titles and labels
- Export capabilities for figures and results
- Performance considerations for large datasets

## Submission Process

### Before Submitting

1. **Test Your Changes**
   ```bash
   # Run existing scripts to ensure they still work
   python scripts/copying.py --help
   
   # Test any new functionality
   python your_new_script.py
   ```

2. **Update Documentation**
   - Update relevant README sections
   - Document new scripts in `scripts/ABOUT.md`
   - Add usage examples where appropriate

3. **Check File Organization**
   - Ensure no temporary files are included
   - Verify proper file permissions
   - Check that large files are appropriately placed

### Pull Request Process

1. **Create Pull Request**
   - Use descriptive title and description
   - Reference any related issues
   - Include screenshots for UI changes
   - List all files changed and why

2. **Pull Request Template**
   ```markdown
   ## Description
   Brief description of changes

   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Dataset improvement

   ## Testing
   - [ ] Tested locally
   - [ ] All existing scripts still work
   - [ ] New functionality tested

   ## Documentation
   - [ ] Updated relevant documentation
   - [ ] Added usage examples
   - [ ] Updated requirements if needed
   ```

3. **Review Process**
   - Address reviewer feedback promptly
   - Make requested changes in the same branch
   - Ensure all tests pass
   - Maintain clean commit history

## Dataset License and Ethics

### Image Licensing
- Only contribute images with CC-compatible licenses
- Provide source attribution when possible
- Verify you have rights to contribute images
- Do not include copyrighted material without permission

### Ethical Considerations
- Respect privacy in public space imagery
- Avoid including identifiable people or private property
- Consider geographic and cultural diversity
- Maintain objectivity in image selection

## Community Guidelines

### Communication
- Be respectful and constructive in discussions
- Ask questions if guidelines are unclear
- Provide helpful feedback on others' contributions
- Use GitHub issues for bug reports and feature requests

### Collaboration
- Coordinate on large changes through issues
- Share knowledge and expertise freely
- Help newcomers understand the project
- Acknowledge others' contributions

## Recognition

Contributors will be acknowledged in:
- Repository contributors list
- Release notes for significant contributions
- Academic papers using the dataset (when appropriate)
- Special recognition for outstanding contributions

## Questions and Support

- **General Questions**: Open a GitHub issue with the `question` label
- **Bug Reports**: Use the `bug` label with detailed reproduction steps
- **Feature Requests**: Use the `enhancement` label with clear descriptions
- **Documentation Issues**: Use the `documentation` label

## Development Roadmap

Current priorities for contributions:
1. Expanding dataset size and diversity
2. Improving analysis tool capabilities
3. Adding comprehensive testing
4. Creating tutorial materials
5. Developing model benchmarking tools

Thank you for contributing to the Deep Pavements Dataset! Your contributions help advance research in computer vision and pavement surface analysis.