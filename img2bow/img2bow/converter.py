from PIL import Image, ImageFilter

def convert_to_black_and_white(image_path, output_path, threshold=128):
    """
    Converts an image to black and white, applies a Gaussian blur,
    resizes it to a maximum of (1000, 200) while maintaining aspect ratio,
    centers it on a white canvas, and saves the result.

    :param image_path: String path to the input image.
    :param output_path: String path to the output image.
    :param threshold: Intensity threshold for black/white conversion. Defaults to 128.
    """
    image = Image.open(image_path).convert('L')
    image = image.filter(ImageFilter.GaussianBlur(radius=2))
    binary_image = image.point(lambda p: p > threshold and 255)
    max_size = (1000, 200)
    binary_image.thumbnail(max_size, Image.Resampling.LANCZOS)
    resized_image = Image.new('L', max_size, 255)

    offset_x = (max_size[0] - binary_image.width) // 2
    offset_y = (max_size[1] - binary_image.height) // 2
    resized_image.paste(binary_image, (offset_x, offset_y))
    resized_image.save(output_path, optimize=True)