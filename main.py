# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot





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
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	

	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)
	ship = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)) # Object is used via groups
	space = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill("black")

		updatable.update(dt)

	
		for asteroid in asteroids:
			if not asteroid.collision(ship):
				print("Game over!")
				sys.exit(1)

			
		for drawbales in drawable:
			drawbales.draw(screen)

		if pygame.key.get_pressed()[pygame.K_SPACE]:
			ship.shoot(shots)	

		pygame.display.flip()
		frames_per_second.tick(60)
		dt = (frames_per_second.get_time() / 1000)



if __name__ == "__main__":
	main()
