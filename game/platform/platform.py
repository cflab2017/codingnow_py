import pygame
import pygame.sprite
import traceback

from codingnow.game.platform.player import *
from codingnow.game.platform.block import *
from codingnow.game.platform.coin import *
from codingnow.game.platform.monster import *
from codingnow.game.platform.lava import *
from codingnow.game.platform.bullet import *
from codingnow.game.platform.exitdoor import *

class Platform():
    player:Player = None
    def __init__(self,screen:Surface) -> None:
        self.screen = screen
        self.group_block = pygame.sprite.Group()
        self.group_coin = pygame.sprite.Group()
        self.group_lava = pygame.sprite.Group()
        self.group_monster = pygame.sprite.Group()
        self.group_exitDoor = pygame.sprite.Group()
        self.group_bullet = pygame.sprite.Group()
        self.image_bg = None
        self.map_data = {}
    

    def map_change(self):
        self.group_bullet.empty()
        self.group_coin.empty()
        self.group_monster.empty()
        self.group_block.empty()
        self.group_lava.empty()
        self.group_exitDoor.empty()
        try:            
            if self.player.level not in self.map_data:
                self.player.level = 1
                
            if self.player.level not in self.map_data:
                return
            
            for key in self.map_data[self.player.level]:
                item = self.map_data[self.player.level][key]
                
                for values in item:
                    filename = values[0]
                    x  = values[1]
                    y  = values[2]                        
                    if key == 'block':
                        move_x = values[3] 
                        move_y = values[4]
                        self.group_block.add(Block(self.screen,filename,x,y,move_x,move_y))
                    if key == 'coin':
                        self.group_coin.add(Coin(self.screen,filename,x,y))
                    if key == 'monster':
                        self.group_monster.add(Monster(self.screen,filename,x,y))
                    if key == 'exit':
                        self.group_exitDoor.add(ExitDoor(self.screen,filename,x,y))
                    if key == 'lava':
                        self.group_lava.add(Lava(self.screen,filename,x,y))
        except Exception as ex:
            print(ex)
                        
    def add_player(self,filename:str, width:int, height:int):
        self.player = Player(self,self.screen,filename,width,height)
        return self.player
    
    def add_bg_image(self,filename:str):        
        img = pygame.image.load(f'{filename}').convert_alpha()
        self.image_bg = pygame.transform.scale(img,(self.screen.get_width(),self.screen.get_height()))

    def check_map_init(self, level, key):
        if level not in self.map_data:
            self.map_data.update({level:{}})
        if key not in self.map_data[level]:
            self.map_data[level].update({key:[]})
        
    def add_map_block(self,level:int, filename:str, x:int, y:int,move_x:int=0,move_y:int=0):
        self.check_map_init(level,'block')            
        self.map_data[level]['block'].append([filename,x,y,move_x,move_y])
        
    def add_map_coin(self,level:int, filename:str, x:int, y:int):
        self.check_map_init(level,'coin')            
        self.map_data[level]['coin'].append([filename,x,y])        
                
    def add_map_mons(self,level:int, filename:str, x:int, y:int):
        self.check_map_init(level,'monster')
        self.map_data[level]['monster'].append([filename,x,y])
        
    def add_map_lava(self,level:int, filename:str, x:int, y:int, num:int):
        self.check_map_init(level,'lava')        
        for i in range(num):
            self.map_data[level]['lava'].append([filename,x+30*i,y])
        
    def add_map_exit(self,level:int, filename:str, x:int, y:int):
        self.check_map_init(level,'exit')
        self.map_data[level]['exit'].append([filename,x,y])


    def add_bullet(self,images):
        self.group_bullet.add(Bullet(self.screen,images,self.player))
    
    def draw(self):
        if self.image_bg is not None:
            self.screen.blit(self.image_bg,(0,0))
        if self.player is not None:            
            self.player.draw()
            
        for bullet in self.group_bullet:
            if pygame.sprite.spritecollide(bullet, self.group_monster, True):
                bullet.kill()
                self.player.score += 20
                if self.player.snd_dic['monster'] is not None:
                    self.player.snd_dic['monster'].play()
        
        self.group_block.update()
        self.group_coin.update()
        self.group_monster.update()
        self.group_lava.update()
        self.group_bullet.update()
        self.group_exitDoor.update()
        
        self.group_exitDoor.draw(self.screen)
        self.group_block.draw(self.screen)
        self.group_coin.draw(self.screen)
        self.group_monster.draw(self.screen)
        self.group_lava.draw(self.screen)
        self.group_bullet.draw(self.screen)