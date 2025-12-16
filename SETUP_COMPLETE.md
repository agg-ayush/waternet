# ✅ WaterNet Inference Setup Complete

This is a clean, minimal setup of **tnwei/waternet** configured for inference only.

## What Was Done

✓ Cloned fresh repo from [tnwei/waternet](https://github.com/tnwei/waternet)  
✓ Downloaded pretrained weights (4.4 MB)  
✓ Renamed weights to: `pretrained-waternet.pt`  
✓ Removed training files (`train.py`, `score.py`)  
✓ Removed documentation and config files  
✓ Created simple wrapper script: `infer.py`  
✓ Added quick start guide  

## What's Included

- **infer.py** - Simple wrapper for inference
- **inference.py** - Main inference script (from upstream)
- **pretrained-waternet.pt** - Model weights
- **waternet/** - Core WaterNet module
- **requirements.txt** - Dependencies
- **QUICKSTART.md** - Usage guide

## What Was Removed

- `train.py` - Training script
- `score.py` - Scoring script
- `colab-example-waternet.ipynb` - Colab notebook
- `hubconf.py` - PyTorch hub config
- `docs/` - Documentation folder
- `.git/` - Git history
- Config files: `env.yaml`, `env-training.yaml`, `.pre-commit-config.yaml`, `.gitlint`

## How to Use

### Install
```bash
pip install -r requirements.txt
```

### Run Inference

```bash
# Single image
python3 infer.py --input image.jpg

# Folder
python3 infer.py --input ./images/ --output ./results/

# With before/after view
python3 infer.py --input image.jpg --show-split
```

### Results
Enhanced images are saved to `output/` folder by default.

## Key Features

✓ Automatic GPU/CPU detection  
✓ Batch processing (images & videos)  
✓ Before/after visualization option  
✓ Custom checkpoint support  
✓ Supports: JPG, PNG, BMP, GIF, MP4, AVI, MPEG  

## Ready to Use! 🚀

Start by running:
```bash
python3 infer.py --input your_underwater_image.jpg
```

See [QUICKSTART.md](QUICKSTART.md) for more examples.
