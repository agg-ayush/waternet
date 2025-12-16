# WaterNet - Inference Only Setup

Clean, minimal setup for underwater image enhancement using pretrained WaterNet weights.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Inference

**Single image:**
```bash
python3 infer.py --input photo.jpg
```

**Folder of images:**
```bash
python3 infer.py --input ./underwater_images/ --output ./enhanced/
```

**With before/after visualization:**
```bash
python3 infer.py --input image.jpg --show-split
```

## Output

Enhanced images are saved to `output/` folder (or custom folder with `--output`).

## Usage Guide

### Basic Command
```bash
python3 infer.py --input <path>
```

### Options
- `--input PATH` - Input image/video or folder (required)
- `--output FOLDER` - Output folder (default: `output`)
- `--weights PATH` - Pretrained weights file (default: `pretrained-waternet.pt`)
- `--show-split` - Show before/after split view

## Project Structure

```
waternet/
├── infer.py                    # Simple wrapper script (use this!)
├── inference.py                # Main inference script
├── pretrained-waternet.pt      # Model weights (4.4 MB)
├── requirements.txt            # Dependencies
├── waternet/                   # WaterNet module
└── README.md                   # Original project info
```

## Pretrained Weights

- File: `pretrained-waternet.pt` (4.4 MB)
- Source: [tnwei/waternet](https://github.com/tnwei/waternet)
- Based on: IEEE TIP 2019 WaterNet paper

## Model Details

- **Input**: Underwater RGB images (any resolution)
- **Output**: Enhanced RGB images
- **Framework**: PyTorch
- **Device**: Auto-detects GPU/CPU

## Examples

```bash
# Enhance a single underwater photo
python3 infer.py --input underwater_photo.jpg

# Batch process a folder
python3 infer.py --input ./raw_images/ --output ./enhanced_images/

# Save with before/after comparison
python3 infer.py --input image.jpg --show-split

# Use custom checkpoint
python3 infer.py --input image.jpg --weights ./custom_model.pt
```

## Supported Formats

**Images**: bmp, jpg, jpeg, png, gif  
**Videos**: mp4, mpeg, avi

---

For detailed information, see the [original README.md](README.md)
