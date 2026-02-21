import pygame
import pygame.font

pygame.init()
pygame.font.init()

class menuItem():
    def __init__(self, text, x, y, scalex,scaley, path):
        self.x = x
        self.y = y
        self.text = text
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image,(scalex,scaley))
        self.rect = self.image.get_rect()
        
    def click(self):
        pass

    def update(self, window):
        self.rect.center = (self.x, self.y)
        self.draw(window)

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
        
    def update(self,window):
        self.items = self.sections[self.page]
        self.draw_header(window, 100)

        for item in self.items:
            item.update(window)
        
        self.mousex, self.mousey = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed():
            pass
    
    def draw_header(self,window,size):
        self.font = pygame.font.SysFont("Times New Roman",size)
        self.text = self.font.render(self.headers[self.page],True,(255,255,255))
        window.blit(self.text, self.text.get_rect(center=(window.get_width()/2,size)))
        

# above is the framework, below is actual implementation

class window():
    def __init__(self, width, height):
        self.running = True
        self.window = pygame.display.set_mode((width,height), pygame.RESIZABLE)

        self.middlex = self.window.get_width()/2
        self.middley = self.window.get_height()/2

        self.menu = menu([[menuItem(None,self.middlex,300, 200, 80,"Example Assets\\testbutton.png"),
                           menuItem(None,self.middlex,500, 200, 80, "Example Assets\\testbutton.png")]],
                           ["Test Header"])

        self.main()

    def main(self):
        while self.running == True:
            self.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
    
    def update(self):
        self.window.fill((0,0,0))
        self.menu.update(self.window)
        pygame.display.flip()
    

w = window(1000,1000)