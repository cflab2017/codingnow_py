import pygame
from pygame.locals import *
from pygame import Surface

class DrawMsg():
	msg_score_text = None
	msg_level_text = None
	msg_weapon_text = None
	msg_hp_text = None
	def __init__(self,screen:Surface):
		self.screen = screen
		self.mfont = pygame.font.SysFont('malgungothic', 20)
                
	def set_msg_score(self, x=10,y=10, color = (0,0,0), text = '점수 : '):
		self.msg_score_x = x
		self.msg_score_y = y
		self.msg_score_color = color
		self.msg_score_text = text
		
	def set_msg_level(self, x=10,y=50, color = (0,0,0), text = '레벨 : '):
		self.msg_level_x = x
		self.msg_level_y = y
		self.msg_level_color = color
		self.msg_level_text = text
		
	def set_msg_weapon(self, x=10,y=90, color = (0,0,0), text = '레벨 : '):
		self.msg_weapon_x = x
		self.msg_weapon_y = y
		self.msg_weapon_color = color
		self.msg_weapon_text = text
		
	def set_msg_hp(self, x=10,y=130, color = (0,0,0), text = 'HP : '):
		self.msg_hp_x = x
		self.msg_hp_y = y
		self.msg_hp_color = color
		self.msg_hp_text = text
		
	def draw_message(self, msg:str, color:tuple, x:int, y:int):
		msg = f'{msg}'
		img = self.mfont.render(msg, True, color,(0,0,0))
		img.set_alpha(100)
		self.screen.blit(img, (x, y))
    
	def draw(self,score,level,weapons,hp):
		if self.msg_score_text is not None:
			self.draw_message(f'{self.msg_score_text}{score}',
							self.msg_score_color, 
							x=self.msg_score_x,
							y=self.msg_score_y)

		if self.msg_level_text is not None:
			self.draw_message(f'{self.msg_level_text}{level}',
							self.msg_level_color, 
							x=self.msg_level_x,
							y=self.msg_level_y)
			
		if self.msg_weapon_text is not None:
			self.draw_message(f'{self.msg_weapon_text}{weapons}',
							self.msg_weapon_color, 
							x=self.msg_weapon_x,
							y=self.msg_weapon_y)
			
		if self.msg_hp_text is not None:
			self.draw_message(f'{self.msg_hp_text}{hp}',
							self.msg_hp_color, 
							x=self.msg_hp_x,
							y=self.msg_hp_y)