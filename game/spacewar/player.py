import pygame
from pygame.locals import *
from pygame import Surface

from codingnow.game.spacewar.enemy import *
from codingnow.game.spacewar.weapon import *
from codingnow.game.spacewar.items import *

class Player():
	score=0
	hp=100
	level = 1
	level_pre = 1
	
	speed = 2
	weapon_img = None
	weapon_damage = 0
	weapon_speed = 0
	weapon_delay = 0

	weapon_def_img = None
	weapon_def_damage = 0
	weapon_def_speed = 0
	weapon_def_delay = 0
	
	group_weapon = pygame.sprite.Group()
	group_items = pygame.sprite.Group()
	
	game_over = False
	
	def __init__(self,screen:Surface,filename, rect:pygame.Rect, hp = 100,angle=0, flip=False):
		self.screen = screen
		self.filename = filename
		self.hp = hp
		self.hp_start = hp
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
		self.sx = rect.x
		self.sy = rect.y
		self.weapon_tick = 0
		
		self.shield_tick = 0
		self.shield_on = False
		
		self.snd_dic = {
			'shoot':None,
			'hit':None,
			'item':None,
			'shock':None,
			'game_over':None,
		}
		
	def reset(self):
		self.score=0
		self.level = 1
		self.level_pre = 1
		self.hp=self.hp_start
		self.rect.x = self.sx
		self.rect.y = self.sy
		
		self.weapon_img = self.weapon_def_img
		self.weapon_damage = self.weapon_def_damage
		self.weapon_speed = self.weapon_def_speed
		self.weapon_delay = self.weapon_def_delay
		self.group_weapon.empty()
		self.group_items.empty()
		
		self.game_over = False
		
	def check_levelup(self):
		if self.level > self.level_pre:
			self.level_pre = self.level
			return True
		
		self.level_pre = self.level
		return False
	
	def set_snd_shoot(self,filename):
		self.snd_dic['shoot'] = pygame.mixer.Sound(filename)
		
	def set_snd_item(self,filename):
		self.snd_dic['item'] = pygame.mixer.Sound(filename)
		
	def set_snd_hit(self,filename):
		self.snd_dic['hit'] = pygame.mixer.Sound(filename)
		
	def set_snd_game_over(self,filename):
		self.snd_dic['game_over'] = pygame.mixer.Sound(filename)
		
	def set_snd_shock(self,filename):
		self.snd_dic['shock'] = pygame.mixer.Sound(filename)
		
	def set_weapon(self, filename, width, height, damage,speed,delay, flip=False):
		img = pygame.image.load(f'{filename}').convert_alpha()
		img = pygame.transform.scale(img, (width, height))
		if flip:
			img = pygame.transform.flip(img,True,False)
			
		self.weapon_img = img
		self.weapon_damage = damage
		self.weapon_speed = speed*-1
		self.weapon_delay = delay
		
		self.weapon_def_img = self.weapon_img
		self.weapon_def_damage = self.weapon_damage
		self.weapon_def_speed = self.weapon_speed
		self.weapon_def_delay = self.weapon_delay
	
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
			if self.weapon_img is not None:
				if pygame.time.get_ticks() - self.weapon_tick > self.weapon_delay:
					self.weapon_tick = pygame.time.get_ticks()
					cx = self.rect.centerx
					cy = self.rect.centery
					weapon = Weapon(self.screen, self.weapon_img,cx,cy,self.weapon_damage, self.weapon_speed)
					self.group_weapon.add(weapon)
					if self.snd_dic['shoot'] is not None:
						self.snd_dic['shoot'].play()
				
	def draw_shield(self):
		
		if self.shield_on:
			self.shield_tick = pygame.time.get_ticks()
			self.shield_on = False
			
		if self.shield_tick > 0:
			ellip = pygame.time.get_ticks() - self.shield_tick
			if ellip < 500:
				temp_surface = pygame.Surface(self.image.get_size())
				temp_surface.fill((255, 0, 255))
				temp_surface.blit(self.image, (0, 0))
				temp_surface.set_alpha(80)
				self.screen.blit(temp_surface, self.rect)
			else:
				self.shield_tick = 0
            
	def draw(self,group_enemy:pygame.sprite.Group):
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
			
		items = pygame.sprite.spritecollide(self,self.group_items,True)	
		for item in items:
			self.hp += item.hp
			if item.weapon_img is not None:
				self.weapon_img = item.weapon_img
				self.weapon_damage = item.weapon_damage
				self.weapon_delay = item.weapon_delay
			if self.snd_dic['item'] is not None:
				self.snd_dic['item'].play()
			# self.weapon_speed = item.speed*-1
		
		for enemy in group_enemy:			
			# if pygame.sprite.spritecollide(self,enemy.group_weapon,True):
			for w_weapon in enemy.group_weapon:
				if self.rect.colliderect(w_weapon.rect):
					self.hp -= w_weapon.damage
					self.shield_on = True
					w_weapon.kill()

					if self.hp <= 0:
						self.hp = 0		
						self.game_over = True
						if self.snd_dic['game_over'] is not None:
							self.snd_dic['game_over'].play()
					else:
						if self.snd_dic['shock'] is not None:
							self.snd_dic['shock'].play()
				else:
					if pygame.sprite.spritecollide(w_weapon,self.group_weapon,True):
						w_weapon.kill()
						
						if self.snd_dic['hit'] is not None:
							self.snd_dic['hit'].play()
			
			weapons = pygame.sprite.spritecollide(enemy,self.group_weapon,False)			
			for weapon in weapons:
				pygame.sprite.spritecollide(weapon,enemy.group_weapon,True)
				enemy.hp -= weapon.damage
				enemy.shield_on = True
				
				if self.snd_dic['hit'] is not None:
					self.snd_dic['hit'].play()
				if enemy.hp <= 0:
					self.score += enemy.hp_max
										
					if enemy.i_img is not None:
						item = Items(self.screen,
										enemy.i_img,
										enemy.rect.centerx,
										enemy.rect.centery,
										enemy.i_hp,
										enemy.i_weapon_img,
										enemy.i_weapon_damage,
										enemy.i_weapon_delay,
				    						)
						self.group_items.add(item)						
					
					enemy.kill()
					break
				weapon.kill()
			else:
				if self.rect.colliderect(enemy.rect):
					self.hp -= enemy.hp
					self.shield_on = True
					enemy.kill()
					if self.hp <= 0:
						self.hp = 0
						self.game_over = True
						if self.snd_dic['game_over'] is not None:
							self.snd_dic['game_over'].play()
					else:						
						if self.snd_dic['shock'] is not None:
							self.snd_dic['shock'].play()
						
		self.draw_shield()
		self.group_items.update()
		self.group_weapon.update()
		
		self.group_items.draw(self.screen)
		self.group_weapon.draw(self.screen)
		self.screen.blit(self.image,self.rect)
		