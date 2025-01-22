# logo2cc

A PyPi library to convert images to black and white (no gray) to use as custom logos on Stripe credit cards. 

**Processing Pipeline:** Applies a slight Gaussian blur, resizes it to fit a maximum dimension of 1000×200 pixels, and centers it on a white canvas.

## Installation

1. Clone this repository or download the files.
2. In the same directory as `setup.py`, run:
   ```bash
   pip install .
   ```

   or to install in editable mode:

   ```bash
   pip install -e .
   ```

## Usage

```py
from logo2cc.converter import convert_to_black_and_white

# Convert an image to black & white and save it
convert_to_black_and_white("input_image.png", "output_image.png", threshold=128)
```

---

## How to Install and Use

1. **Install**  
   In your terminal, change directory (`cd`) into the location of `setup.py`, then run:
   ```bash
   pip install .
   ```

2. **Import and Call**  
   In your Python script or REPL:
    ```py
    from logo2cc.converter import convert_to_black_and_white

    convert_to_black_and_white("input.png", "output.png", threshold=128)
    ```