
import random
import pygame
from blob_class import Blob
import numpy as np

STARTING_BLUE_BLOBS = 20
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15
#specifying width and height of environment
WIDTH = 800
HEIGHT = 600
#specifying some colours
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN  = (0,255,0)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

class BlueBlob(Blob):
	
	def __init__(self, x_bounds, y_bounds):
		Blob.__init__(self, BLUE, x_bounds, y_bounds)

	def __add__(self, other_blob):
		if (other_blob.color == RED) or (other_blob.color == GREEN):
			other_blob.size += self.size
			self.size = 0
		elif (other_blob.color == BLUE):
			pass
		else:
			raise Exception('Color does not exist.')

class RedBlob(Blob):
	def __init__(self, x_bounds, y_bounds):
		Blob.__init__(self, RED, x_bounds, y_bounds)		
	
class GreenBlob(Blob):
	def __init__(self, x_bounds, y_bounds):
		Blob.__init__(self, GREEN, x_bounds, y_bounds)
	
def istouching(b1,b2):
	""" Checking if two blobs are touching by using the norm or euclidean distance """
	return np.linalg.norm(np.array([b1.x,b1.y])-np.array([b2.x,b2.y])) < (b1.size + b2.size)

def handle_collision(blob_list):
	""" Method which tells what happens if two blobs collide """
	blues, reds, greens = blob_list
	#since we are modifying the blob_list , we need to first copy the list while iterationg trough it
	for blue_id,blue_blob in blues.copy().items():
		for other_blobs in blues,reds,greens:
			for other_blob_id, other_blob in other_blobs.copy().items():
				if blue_blob == other_blob:
					pass
				else:
					if istouching(blue_blob, other_blob):
						blue_blob + other_blob
						if blue_blob.size <= 0:
							del blues[blue_id] #deleting the blue_blob which collided
	return blues, reds, greens 						

def draw_environment(blob_list):
	#paint the environment white every time on starting
	game_display.fill(WHITE)
	blues, reds, greens = handle_collision(blob_list)
	for blob_dict in blob_list:
		for blob_id in blob_dict:
			blob = blob_dict[blob_id]
			#displaying our blob on the environment
			pygame.draw.circle(game_display, blob.color, [blob.x,blob.y], blob.size)
			#moving the blob in environment
			blob.move() #method taken from BlueBlob class
	pygame.display.update()
	return blues, reds, greens 


def main():
	#creating a dictionary so we will have id for each blob
	blue_blobs = dict(enumerate([BlueBlob(WIDTH,HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
	red_blobs = dict(enumerate([RedBlob(WIDTH,HEIGHT) for i in range(STARTING_RED_BLOBS)]))
	green_blobs = dict(enumerate([GreenBlob(WIDTH,HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit() #quit the gane if window/environment is closed
				quit()
		
		blue_blobs, red_blobs, green_blobs	= draw_environment((blue_blobs, red_blobs, green_blobs))
		clock.tick(60)

if __name__ == '__main__':
	main()