#!/usr/bin/env python3
"""
Simplified WaterNet inference script
Usage: python3 infer.py --input <image_or_folder> [--output results] [--weights pretrained-waternet.pt]
"""

import argparse
import sys
from pathlib import Path
import subprocess

def main():
    parser = argparse.ArgumentParser(
        description='Run WaterNet inference on underwater images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 infer.py --input photo.jpg
  python3 infer.py --input ./underwater_images/ --output ./enhanced/
  python3 infer.py --input images/ --weights custom_weights.pt
        """
    )
    
    parser.add_argument('--input', type=str, required=True,
                        help='Path to input image/video or folder')
    parser.add_argument('--output', type=str, default='output',
                        help='Output folder (default: output)')
    parser.add_argument('--weights', type=str, default='waternet.pt',
                        help='Path to pretrained weights (default: waternet.pt)')
    parser.add_argument('--show-split', action='store_true',
                        help='Show before/after split in output')
    
    args = parser.parse_args()
    
    # Validate input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input path not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Validate weights
    weights_path = Path(args.weights)
    if not weights_path.exists():
        print(f"Error: Weights not found: {args.weights}", file=sys.stderr)
        sys.exit(1)
    
    # Build inference.py command
    cmd = [
        'python3', 'inference.py',
        '--source', str(input_path),
        '--weights', str(weights_path),
        '--name', args.output
    ]
    
    if args.show_split:
        cmd.append('--show-split')
    
    print(f"Running inference...")
    print(f"  Input: {input_path}")
    print(f"  Weights: {weights_path}")
    print(f"  Output: {args.output}")
    print()
    
    # Run the main inference script
    result = subprocess.run(cmd)
    sys.exit(result.returncode)

if __name__ == '__main__':
    main()
