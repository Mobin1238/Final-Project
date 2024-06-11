from PIL import Image, ImageOps
import numpy as np

def convolve2d(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    output_height, output_width = image_height - kernel_height + 1, image_width - kernel_width + 1
    
    return np.array([
        [np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel) 
         for j in range(output_width)] 
        for i in range(output_height)
    ])

image_path = 'c:\\Users\\Rayan system\\Desktop\\m-270170697752965be68f9a096e.jpeg'

image = np.array(Image.open(image_path).convert('L'))

# تعریف فیلترهای Sobel
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])


edges_x = convolve2d(image, sobel_x)
edges_y = convolve2d(image, sobel_y)

edges = np.hypot(edges_x, edges_y)

edges_image = Image.fromarray(np.uint8(edges))

output_path = 'C:\\Users\\Rayan system\\Desktop\\Mobin_Final\\Mobin_Final\\output.png'

edges_image.save(output_path)

print(f"خروجی به عنوان تصویر در مسیر '{output_path}' ذخیره شد.")
