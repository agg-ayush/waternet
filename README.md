# WaterNet - Underwater Image Enhancement

A PyTorch implementation of WaterNet for underwater image enhancement, based on "An Underwater Image Enhancement Benchmark Dataset and Beyond" (IEEE TIP 2019).

This is a streamlined, production-ready version focused on inference with pretrained weights.

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

Enhance a single underwater image:
```bash
python infer.py --input photo.jpg
```

Process multiple images:
```bash
python infer.py --input ./underwater_images/ --output ./enhanced/
```

View before/after split:
```bash
python infer.py --input image.jpg --show-split
```

Enhanced images are saved to `output/` folder.

## Advanced Usage

### Via Command Line

```bash
python inference.py --source <path> [--weights <model>] [--name <subfolder>] [--show-split]
```

Options:
- `--source` - Input image/video/directory
- `--weights` - Path to model weights (optional, downloads pretrained if not specified)
- `--name` - Output subfolder name
- `--show-split` - Show before/after comparison

### Via Python

```python
import torch
import cv2

# Load pretrained weights
preprocess, postprocess, model = torch.hub.load('tnwei/waternet', 'waternet')
model.eval()

# Process image
im = cv2.imread("example.png")
rgb_im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

rgb_ten, wb_ten, he_ten, gc_ten = preprocess(rgb_im)
out_ten = model(rgb_ten, wb_ten, he_ten, gc_ten)
out_im = postprocess(out_ten)
```

## How It Works

WaterNet is a gated fusion network designed to reverse the effects of underwater light scattering through image-to-image translation.

### Architecture

1. **Input Refinement**: Generates refined versions of the input using multiple transformations:
   - White balance correction
   - Gamma correction
   - Histogram equalization

2. **Confidence Map Generation**: Creates three confidence maps for weighted combination

3. **Output Fusion**: Combines refined inputs using confidence maps for final enhanced image

### Dataset

The model is trained on the UIEB (Underwater Image Enhancement Benchmark) dataset, which provides paired original and reference underwater images.

Reference: [Li et al., IEEE TIP 2019](https://arxiv.org/abs/1901.05495)

## Project Files

- `infer.py` - Simple inference script (recommended for basic use)
- `inference.py` - Full-featured inference with more options
- `waternet/net.py` - WaterNet model architecture
- `waternet/data.py` - Data loading and preprocessing
- `waternet/training_utils.py` - Training utilities

## Requirements

- Python 3.7+
- PyTorch
- OpenCV
- NumPy

See `requirements.txt` for full dependencies.

## License

Based on the original WaterNet implementation.
