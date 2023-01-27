import pygame
import sys
import random

# initialize pygame
pygame.init()

# load image file taken from command line into memory
img_src = pygame.image.load(sys.argv[1])

# retrieve the width and height value of the loaded image file
(w,h) = img_src.get_size()

# create a pygame window surface
win_sfc = pygame.display.set_mode((8*w,8*h))

# set backgroud colour to white
win_sfc.fill((255,255,255))

# outer count-controlled loop controls the height (i.e. rows)
for y in range(h):
	# inner count-controlled loop controls the width (i.e. columns)
	for x in range(w):
		# retrieve (R,G,B) value from specific pixel at location (x,y)
		(r,g,b,_) = img_src.get_at((x,y))
		
		# determine the lowest common multiple of the three r,g,b values 
		if r < g:
			if r < b:
				factor = r
			else:
				factor = b
		elif g < b:
			factor = g
		else:
			factor = b
	
		# divide (R,G,B) values by factor to determine appropriate number of red, green, and blue pixels to draw on scaled image
		num_reds = int(r/(factor+1))		
		num_greens = int(g/(factor+1))		
		num_blues = int(b/(factor+1))
		
		# print num_reds value's worth of red pixels 
		for i in range(num_reds):
			# set (x,y) position of rectangle to be a random x and random y between the appropriate scaled up dimensions of the new image
			pygame.draw.rect(win_sfc, (r,0,0), (random.randint(8*x, (8*x)+8),random.randint(8*y, (8*y)+8), 4, 4))
		# print num_greens value's worth of green pixels 
		for j in range(num_greens):
			# set (x,y) position of rectangle to be a random x and random y between the appropriate scaled up dimensions of the new image
			pygame.draw.rect(win_sfc, (0,g,0), (random.randint(8*x, (8*x)+8),random.randint(8*y, (8*y)+8), 4, 4))
		# print num_blues value's worth of blue pixels 
		for k in range(num_blues):
			# set (x,y) position of rectangle to be a random x and random y between the appropriate scaled up dimensions of the new image
			pygame.draw.rect(win_sfc, (0,0,b), (random.randint(8*x, (8*x)+8),random.randint(8*y, (8*y)+8), 4, 4))
			
# update display 
pygame.display.update()

# delay window surface from closing by 7 seconds
pygame.time.delay(7000)

# save current window surface as a .jpg image
pygame.image.save(win_sfc, "scaled_image.jpg")		

