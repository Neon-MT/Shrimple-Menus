import pygame
from Menu import *

class window():
    def __init__(self, width, height):
        self.running = True
        self.window = pygame.display.set_mode((width,height), pygame.RESIZABLE)

        self.middlex = self.window.get_width()/2
        self.middley = self.window.get_height()/2

        page1 = [menuItem(None,self.middlex,300, 200, 80,"Example Assets\\testbutton.png",1),
                menuItem(None,self.middlex,500, 200, 80, "Example Assets\\testbutton.png",2)]
        
        page2 = [menuItem(None,self.middlex,300, 200, 80,"Example Assets\\testbutton.png",0)]

        page3 = [menuItem(None,self.middlex,300, 200, 80,"Example Assets\\testbutton.png",0)]
        
        self.menu = menu([page1, page2, page3],
                           ["Page 1","Page 2","Page 3"])

        self.main()

    def main(self):
        while self.running == True:
            self.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu.click()
    
    def update(self):
        self.window.fill((0,0,0))
        self.menu.update(self.window)
        pygame.display.flip()
    

w = window(1000,1000)