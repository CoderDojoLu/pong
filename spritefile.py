import pygame
from pygame import *
from random import randint
class ball(pygame.sprite.Sprite):
	def __init__(self, w, h):
		super().__init__()
		self.width=20
		self.height=20
		self.x=randint(0, w-self.width)
		self.y=randint(0, h-self.height)
		self.vx=3
		self.vy=3
		self.x_max = w
		self.y_max = h
		color = white
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.move_right = True
		self.move_down = True
		self.rect.x = self.x
		self.rect.y = self.y
	def update(self):
		self.y += self.vy
		self.x += self.vx
		if self.x>=self.x_max:
			self.vx=-self.vx
		if self.y>=self.y_max: 
			self.vy=-self.vy
		if self.x<=0:
			self.vx=-self.vx
		if self.y<=0:
			self.vy=-self.vy
		print (self.x,self.y,self.vx,self.vy) 
		self.rect.x = self.x
		self.rect.y = self.y
		

class racket(pygame.sprite.Sprite):
	def __init__(self, x, y, color):
		super().__init__()
		pygame.mouse.set_visible(0)
		self.x=x
		self.y=y
		self.width=30
		self.height=60
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.mouse_xy = pygame.mouse.get_pos()
		self.rect.x = self.mouse_xy[0]
		self.rect.y = self.mouse_xy[1]
		
	def update(self):
		self.mouse_xy = pygame.mouse.get_pos() 
		self.x = self.mouse_xy[0]
		self.y = self.mouse_xy[1]
		#if self.x>=self.x_max:
		#	self.vx=-self.vx
		#if self.y>=self.y_max: 
		#	self.vy=-self.vy
		#if self.x<=0:
		#	self.vx=-self.vx
		#if self.y<=0:
		#	self.vy=-self.vy
		#print (self.x,self.y,self.vx,self.vy)
		self.rect.x = self.x
		self.rect.y = self.y
		

class target(pygame.sprite.Sprite):
	def __init__(self, x, y):
		self.x=x
		self.y=y
		self.width=30
		self.height=30
		self.image = pygame.Surface([self.width, self.height])
		self.image.fill(color)
		self.rect = self.image.get_rect()


if __name__=="__main__":
	import pygame

	pygame.init()
	white = (255,255,255)
	black = (0,0,0)
	window = pygame.display.set_mode((800,600))
	clock = pygame.time.Clock()
	ball = ball(800,600)
	racket = racket(400,300,(50,150,255))
	all_sprites = pygame.sprite.Group()
	all_sprites.add(ball)
	all_sprites.add(racket)

	background = pygame.Surface(window.get_size())
	
	while True:
		for i in pygame.event.get():
			if i.type == QUIT:
				exit()
		window.fill(black)
		all_sprites.update()
		all_sprites.draw(window)
		clock.tick(30)
		pygame.display.flip()