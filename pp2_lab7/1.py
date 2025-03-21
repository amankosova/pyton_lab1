import pygame 
pygame.init()
win=pygame.display.set_mode((1000,800))
pygame.display.set_caption("lab7,clock")
a=1
while a:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            a=0
pygame.quit()