#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "pillow>=11.0.0",
# ]
# ///
"""
Apply consistent sepia tone to images for the family recipes site.

This script ensures all header images have a uniform vintage, pen-and-ink sketch
aesthetic by applying a standard sepia tone filter. This creates visual consistency
across the site regardless of the source of the original AI-generated illustrations.

NAMING CONVENTION:
    Images matching the pattern 'header-*.png' in assets/images/ are automatically
    processed. This convention allows for future GitHub Actions automation where
    any newly added header images will be automatically sepia-toned on commit.

LOCAL USAGE:
    # Process all header-*.png files in assets/images/ (default behavior)
    uv run scripts/apply-sepia.py

    # Process specific files
    uv run scripts/apply-sepia.py assets/images/header-home.png

    # Modify files in place (replaces originals)
    uv run scripts/apply-sepia.py --inplace

    # Adjust sepia intensity (0.0 = none, 1.0 = full, default: 0.8)
    uv run scripts/apply-sepia.py --intensity 0.6 --inplace

    # Preview results without modifying originals (creates *-sepia.png files)
    uv run scripts/apply-sepia.py

GITHUB ACTIONS USAGE:
    This script is designed to be callable from GitHub Actions. Future automation
    could detect new header-*.png files and ensure consistent styling:

    - name: Apply sepia to header images
      run: |
        uv run scripts/apply-sepia.py --inplace
        git add assets/images/header-*.png
        git commit -m "Apply consistent sepia tone to headers" || true

TECHNICAL DETAILS:
    Converts image to grayscale first, then applies sepia tint for a classic
    vintage photograph aesthetic with maximum uniformity:

    Step 1 - Convert to grayscale (luminosity method):
        Gray = R * 0.299 + G * 0.587 + B * 0.114

    Step 2 - Apply sepia tint to grayscale:
        R' = Gray
        G' = Gray * 0.95
        B' = Gray * 0.82

    This grayscale-first approach ensures all images have identical sepia tones
    regardless of their original colors, creating maximum visual consistency.

    The intensity parameter allows blending between the original and sepia-toned
    versions for fine-tuning the effect.

DEFAULT SETTINGS:
    - Intensity: 0.8 (strong but not overpowering sepia effect)
    - Pattern: header-*.png in assets/images/
    - Output: Creates *-sepia.png files unless --inplace is specified
"""

import argparse
from pathlib import Path
from PIL import Image
import sys


def apply_sepia(image_path: Path, output_path: Path, intensity: float = 0.8) -> None:
    """
    Apply sepia tone to an image using grayscale-first method.

    Args:
        image_path: Path to input image
        output_path: Path to save sepia-toned image
        intensity: Sepia intensity from 0.0 (no effect) to 1.0 (full sepia)
    """
    # Open the image
    img = Image.open(image_path)

    # Convert to RGB if needed (handles RGBA, L, etc.)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Get pixel data
    pixels = img.load()
    width, height = img.size

    # Apply sepia tone to each pixel
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            # Step 1: Convert to grayscale using luminosity method
            gray = int((r * 0.299) + (g * 0.587) + (b * 0.114))

            # Step 2: Apply sepia tint to grayscale value
            tr = gray
            tg = int(gray * 0.95)
            tb = int(gray * 0.82)

            # Clamp values to 0-255 (should be unnecessary but safe)
            tr = min(255, tr)
            tg = min(255, tg)
            tb = min(255, tb)

            # Blend with original based on intensity
            if intensity < 1.0:
                tr = int(r + (tr - r) * intensity)
                tg = int(g + (tg - g) * intensity)
                tb = int(b + (tb - b) * intensity)

            pixels[x, y] = (tr, tg, tb)

    # Save the result
    img.save(output_path, 'PNG')
    print(f"✓ Sepia applied: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Apply sepia tone to header images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='Image files to process (default: all header-*.png in assets/images/)'
    )
    parser.add_argument(
        '--intensity',
        type=float,
        default=0.8,
        help='Sepia intensity from 0.0 to 1.0 (default: 0.8)'
    )
    parser.add_argument(
        '--output-suffix',
        default='-sepia',
        help='Suffix for output files (default: -sepia)'
    )
    parser.add_argument(
        '--inplace',
        action='store_true',
        help='Modify files in place instead of creating new files'
    )

    args = parser.parse_args()

    # Validate intensity
    if not 0.0 <= args.intensity <= 1.0:
        print("Error: intensity must be between 0.0 and 1.0", file=sys.stderr)
        sys.exit(1)

    # Determine which files to process
    if args.files:
        image_files = [Path(f) for f in args.files]
    else:
        # Default: process all header-*.png in assets/images/
        images_dir = Path('assets/images')
        if not images_dir.exists():
            print(f"Error: {images_dir} not found", file=sys.stderr)
            sys.exit(1)
        image_files = sorted(images_dir.glob('header-*.png'))

    if not image_files:
        print("No image files found to process", file=sys.stderr)
        sys.exit(1)

    print(f"Processing {len(image_files)} image(s) with intensity {args.intensity}...")

    # Process each image
    for img_path in image_files:
        if not img_path.exists():
            print(f"Warning: {img_path} not found, skipping", file=sys.stderr)
            continue

        # Determine output path
        if args.inplace:
            output_path = img_path
        else:
            output_path = img_path.parent / f"{img_path.stem}{args.output_suffix}{img_path.suffix}"

        try:
            apply_sepia(img_path, output_path, args.intensity)
        except Exception as e:
            print(f"Error processing {img_path}: {e}", file=sys.stderr)
            continue

    print("\nDone!")


if __name__ == '__main__':
    main()
