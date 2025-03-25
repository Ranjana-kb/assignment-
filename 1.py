"""
QN:Write a python function to shrink an image by a given factor. The function suppose to builds and returns a new image which is smaller copy of the argument image, by the factor argument.(2023 MAY)

"""
from images import Image

def shrink(image,f):
    old_width = image.getWidth()
    old_height = image.getHeight()
    
    new_width = old_width // 2
    new_height = old_height // 2
    
    new_image = Image(new_width, new_height)  # Create a new smaller image

    for y in range(new_height):
        for x in range(new_width):
            # Get 2x2 pixel block
            (r1, g1, b1) = image.getPixel(2 * x, 2 * y)
            (r2, g2, b2) = image.getPixel(2 * x + 1, 2 * y)
            (r3, g3, b3) = image.getPixel(2 * x, 2 * y + 1)
            (r4, g4, b4) = image.getPixel(2 * x + 1, 2 * y + 1)

            # Compute the average color
            r_avg = (r1 + r2 + r3 + r4) // 4
            g_avg = (g1 + g2 + g3 + g4) // 4
            b_avg = (b1 + b2 + b3 + b4) // 4

            # Set pixel in the new image
            new_image.setPixel(x, y, (r_avg, g_avg, b_avg))

    new_image.draw()  
    new_image.save(f)
# Load and display the original image
f = "leo.gif"
i = Image(f)
shrink(i,f)
