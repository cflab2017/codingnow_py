import pygame
from pygame.locals import *
from pygame import Surface

class DrawBg():
	def __init__(self,screen:Surface,filename, rect:pygame.Rect):
		self.screen = screen
		self.filename = filename
		img = pygame.image.load(f'{filename}')
		self.image = pygame.transform.scale(img, (rect.width, rect.height))
		self.rect = self.image.get_rect()
		self.rect.x = rect.x
		self.rect.y = rect.y
		self.rect2 = self.rect.copy()
		self.width = rect.width

	def draw(self):
		# pygame.draw.rect(self.screen,(255,255,255),rect,1)  
		
		self.rect.x += 1
		if self.rect.x >= self.width:
			self.rect.x = 0
		self.rect2.right = self.rect.left
		
		self.screen.blit(self.image,self.rect2)
		self.screen.blit(self.image,self.rect)