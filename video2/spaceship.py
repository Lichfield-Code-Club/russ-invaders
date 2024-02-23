import pygame
from pygame.locals import *
"""
http://www.codingwithruss.com/gamepage/Invaders/
https://www.youtube.com/watch?v=f4coFYbYQzw&list=PLjcN1EyupaQkAQyBCYKyf1jt1M1PiRJEp&pp=iAQB
"""

pygame.init()

#define fps
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invanders')

#define colours
red = (255, 0, 0)
green = (0, 255, 0)

#load image
bg = pygame.image.load("img/bg.png")

def draw_bg():
	screen.blit(bg, (0, 0))

#create spaceship class
class Spaceship(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("img/spaceship.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health

	def update(self):
		#set movement speed
		speed = 8
		#set a cooldown variable
		cooldown = 500 #milliseconds
		game_over = 0

		#get key press
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= speed
		if key[pygame.K_RIGHT] and self.rect.right < screen_width:
			self.rect.x += speed

		#draw health bar
		pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
		if self.health_remaining > 0:
			pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))

		#record current time
		time_now = pygame.time.get_ticks()
		#shoot
		if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			self.last_shot = time_now

		#update mask
		self.mask = pygame.mask.from_surface(self.image)

		return game_over

#create sprite groups
spaceship_group = pygame.sprite.Group()

#create player
spaceship = Spaceship(screen_width // 2, screen_height - 100,3)
spaceship_group.add(spaceship)

run = True
while run:

	clock.tick(fps)

	#draw background
	draw_bg()

	spaceship.update()
	#draw sprite groups
	spaceship_group.draw(screen)

	#event handlers
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
