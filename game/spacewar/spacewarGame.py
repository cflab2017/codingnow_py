

import os
try:
    import pygame
except:
    os.system('pip install pygame')
    import pygame
    
from pygame.event import Event
from pygame.surface import *

from codingnow.game.spacewar.drawBg import *
from codingnow.game.spacewar.player import *
from codingnow.game.spacewar.drawMsg import *

class SpaceWar():
    player:Player = None
    message:DrawMsg = None
    event_func_p = None
    img_bg = None
    level = 1
    
    def __init__(self,screen:Surface) -> None:
        self.screen = screen
        self.player = None
        self.message = DrawMsg(self.screen)
        pass
    
    def event_func(event:Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # print('aaaa')
                pass
                
    def check_quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.event_func_p is not None:
                self.event_func_p(event)
        return True
    
    def set_msg_score(self, x=10,y=10, color = (0,0,0), text = '점수 : '):
        self.message.set_msg_score(x,y,color,text)
        
    def set_msg_level(self, x=10,y=50, color = (0,0,0), text = '레벨 : '):
        self.message.set_msg_level(x,y,color,text)
        
    def set_msg_weapon(self, x=10,y=90, color = (0,0,0), text = '레벨 : '):
        self.message.set_msg_weapon(x,y,color,text)
        
    def set_msg_hp(self, x=10,y=130, color = (0,0,0), text = 'HP : '):
        self.message.set_msg_hp(x,y,color,text)
          
    def add_bg_image(self, level, filename):
        rect = pygame.Rect(0,0,self.screen.get_width(),self.screen.get_height())
        img = DrawBg(self.screen,filename,rect)
        self.img_bg = img
        
    def set_player(self,filename, x=-1,y=-1,width=100,height=90, angle = 0, flip = False):
        rect = pygame.Rect(x,y,width,height)
        
        if x==-1:
            rect.right = self.screen.get_width()-100
        if y == -1:
            rect.top = self.screen.get_height()-100
            
        self.player = Player(self.screen,filename,rect,angle, flip)
        return self.player
        
    def draw(self):
        if self.img_bg is not None:
            self.img_bg.draw()
        if self.message is not None:
            self.message.draw(score=0,level=1,weapons=1,hp=100)
        if self.player is not None:
            self.player.draw()