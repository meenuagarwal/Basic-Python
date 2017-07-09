
import random
import pygame
from blob_class import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 5
#specifying width and height of environment
WIDTH = 800
HEIGHT = 600
#specifying some colours
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class BlueBlob(Blob):
	""" Child/SubClass of Blob class """
	def __init__(self, color, x_bounds, y_bounds):
		#Using the same init method from super class i.e. Blob class
		#For python 3.x users, using super() function is a way better choice
		Blob.__init__(self,color, x_bounds, y_bounds)
		self.color = BLUE
		#here we overwrite the init method from the super class for our sub-class
	
	def move_fast(self):
		self.x += random.randrange(-7,7)	
		self.y += random.randrange(-7,7)


def draw_environment(blob_list):
	#paint the environment white every time on starting
	game_display.fill(WHITE)
	
	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			#displaying our blob on the environment
			#(x,y) = centre and size = radius
			pygame.draw.circle(game_display, blob.color, [blob.x,blob.y], blob.size)
			#moving the blob in environment
			blob.move_fast() #method taken from BlueBlob class
	
	pygame.display.update()

def main():
	#creating a dictionary so we will have id for each blob
	blue_blobs = dict(enumerate([BlueBlob(BLUE,WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
	red_blobs = dict(enumerate([BlueBlob(RED,WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit() #quit the gane if window/environment is closed
				quit()
		
		draw_environment((blue_blobs, red_blobs))
		clock.tick(60)

if __name__ == '__main__':
	main()