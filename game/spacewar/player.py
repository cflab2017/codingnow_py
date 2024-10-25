import pygame
from pygame.locals import *
from pygame import Surface

class Player():
	speed = 2
	def __init__(self,screen:Surface,filename, rect:pygame.Rect, angle=0, flip=False):
		self.screen = screen
		self.filename = filename
		img = pygame.image.load(f'{filename}').convert_alpha()
		img = pygame.transform.scale(img, (rect.width, rect.height))
		if flip:
			img = pygame.transform.flip(img,True,False)
			
		if angle!=0:
			img = pygame.transform.rotate(img,angle)
			
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = rect.x
		self.rect.y = rect.y
		self.rect2 = self.rect.copy()
            
	def key_pressed(self):
		key_press = pygame.key.get_pressed()
		
		if key_press[pygame.K_UP]:
			self.rect.y -= self.speed
			
		if key_press[pygame.K_DOWN]:
			self.rect.y += self.speed
							
		if key_press[pygame.K_LEFT]:
			self.rect.x -= self.speed
			
		if key_press[pygame.K_RIGHT]:
			self.rect.x += self.speed
			
		if key_press[pygame.K_SPACE]:
			pass
            
	def draw(self):
		# pygame.draw.rect(self.screen,(255,255,255),rect,1)  
		self.key_pressed()
		
		if self.rect.x < 0:
			self.rect.x = 0
		if self.rect.right > self.screen.get_width():
			self.rect.right = self.screen.get_width()
			
		if self.rect.y < 0:
			self.rect.y = 0
		if self.rect.bottom > self.screen.get_height():
			self.rect.bottom = self.screen.get_height()
			
		self.screen.blit(self.image,self.rect)