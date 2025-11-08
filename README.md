# Black and White to Color Animation
A Python script that creates a smooth animated transition between a color image and its grayscale version.

## What It Does

The script loads an image and continuously animates between the original color version and a black-and-white conversion, creating a mesmerizing fade effect that loops indefinitely.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

## How It Works

- **Color to Grayscale Conversion**: Uses standard luminance weights (0.299 R, 0.587 G, 0.114
- **Animation**: Creates 30 frames transitioning from color to grayscale, then 30 frames back
- **Loop**: Repeats indefinitely at 60ms intervals

## Customization
You can adjust the animation by modifying:
- `steps=30` - Number of transition frames
- `interval=60` - Time between frames in milliseconds
- Image filename in the `image_load()` calls
