"""
QN:Write a python function to covert an image to black and white using image processing methods.(2023 MAY)
"""
from images import Image
def bal_w(image):
	blackpixel=(0,0,0)
	whitepixel=(255,255,255)
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(r,g,b)=image.getPixel(x,y)
			avg=(r+g+b)/3
			if avg<128:
				image.setPixel(x,y,blackpixel)
			else:
				image.setPixel(x,y,whitepixel)

f=input("ENTER THE FILENAME:")
i=Image(f)
i.draw()
bal_w(i)
i.draw()
i.save(f+"b&w")
print("IMAGE SAVED SUCCESFULLY")
