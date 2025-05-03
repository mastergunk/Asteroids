# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
#from player import Player2




def main():
	pygame.init()
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	frames_per_second = pygame.time.Clock()
	dt = 0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	#Player2.containers = (updatable, drawable)
	Player.containers = (updatable, drawable)
	ship = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)) # Object is used via groups
	#ship2 = Player2((SCREEN_WIDTH /3), (SCREEN_HEIGHT / 3))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")

		updatable.update(dt)
		
		for drawabales in drawable:
			drawabales.draw(screen)

		pygame.display.flip()
		frames_per_second.tick(60)
		dt = (frames_per_second.get_time() / 1000)



if __name__ == "__main__":
	main()
