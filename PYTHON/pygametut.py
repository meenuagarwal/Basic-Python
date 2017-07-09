import random
import pygame

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

class Blob:

	def __init__(self,color):
		self.x = random.randrange(0,WIDTH)
		self.y = random.randrange(0,HEIGHT)
		self.size = random.randrange(5,15)
		self.color = color

	def move(self):
		self.move_x = random.randrange(-2,3)
		self.move_y = random.randrange(-2,3)
		self.x += self.move_x
		self.y += self.move_y

		#Restricting our blob object to the environment boundary
		if (self.x < 0):
			self.x = 0
		elif (self.x > WIDTH):
			self.x = WIDTH

		if (self.y < 0):
			self.y = 0
		elif (self.y > HEIGHT):
			self.y = HEIGHT


def draw_environment(blobs):
	#paint the environment white every time on starting
	game_display.fill(WHITE)
	#displaying our blob on the environment

	pygame.draw.circle(game_display, blob.color, [blob.x,blob.y], blob.size)
	#moving the blob in environment
	blob.move()
	pygame.display.update()

def main():

	#creating a red blob
	red_blob = Blob(RED)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		
		draw_environment(red_blob)
		clock.tick(60)

if __name__ == '__main__':
	main()