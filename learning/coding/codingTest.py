from codingnow.learning.coding.Chapters.chapter_01 import *
        
class CodingTest:
    chapter = 1
        
    def __init__(self):
        pass
        
    def start(self,chapter):
        self.chapter = chapter
        if self.chapter == 1:
            self.instance = Chapter_01()
            self.instance.start()
        else:
            print("해당 챕터는 준비중입니다.")
    
    def get(self):
        return self.instance.get()
    
    def answer(self, answer):
        return self.instance.answer(answer)
        
    def get_option(self,cmd):
        return self.instance.get_option(cmd)
    
    def print_options(self):
        self.instance.print_options()