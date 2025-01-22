from PIL import Image, ImageFilter

def convert_to_black_and_white(image_path, output_path, threshold=128):
    image = Image.open(image_path).convert('L')
    image = image.filter(ImageFilter.GaussianBlur(radius=2))

    binary_image = image.point(lambda p: p > threshold and 255)

    max_size = (1000, 200)
    binary_image.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    resized_image = Image.new('L', max_size, 255)
    resized_image.paste(
        binary_image, 
        ((max_size[0] - binary_image.width) // 2, (max_size[1] - binary_image.height) // 2)
    )
    
    resized_image.save(output_path, optimize=True)

convert_to_black_and_white('input_image.png', 'output_image.png')
