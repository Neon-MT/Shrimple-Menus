import pygame
import pygame.font

pygame.init()
pygame.font.init()

class menuItem():
    def __init__(self, text, x, y, scalex,scaley, path,nextpage):
        self.x = x
        self.y = y
        self.text = text
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(scalex,scaley))
        self.rect = self.image.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height
        self.nextpage = nextpage
        
    def click(self):
        self.image.set_alpha(0)

    def update(self, window):
        self.rect.center = (self.x, self.y)
        self.draw(window)
        self.image.set_alpha(255)


    def draw(self, window):
        window.blit(self.image, self.rect)



class menu():

    # "secitons" is a list of lists of menu items
    # for example, a menu with 2 sections with 3 buttons each: [[button,button,button],[button,button,button]]

    def __init__(self, sections, headers):
        self.page = 0
        self.sections = sections
        self.headers = headers
        self.pages = len(self.sections)
        self.mouserect = pygame.rect.Rect(0,0,1,1)
        
    def update(self,window):
        self.items = self.sections[self.page]
        self.draw_header(window, 100)

        for item in self.items:
            item.update(window)
        

    
    def draw_header(self,window,size):
        self.font = pygame.font.SysFont("Times New Roman",size)
        self.text = self.font.render(self.headers[self.page],True,(255,255,255))
        window.blit(self.text, self.text.get_rect(center=(window.get_width()/2,size)))

    def click(self):
        self.mousex, self.mousey = pygame.mouse.get_pos()
        self.mouserect.x = self.mousex
        self.mouserect.y = self.mousey
        for item in self.items:
                if pygame.rect.Rect.colliderect(self.mouserect,item.rect):
                    item.click()
                    self.page = item.nextpage
        