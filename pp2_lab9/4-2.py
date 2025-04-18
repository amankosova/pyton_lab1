import pygame 

WIDTH, HEIGHT = 1200, 800  # Ойын терезесінің ені мен биіктігін анықтау
FPS = 90  # Экран жаңарту жылдамдығы
draw = False  # Экранға сурет салу қосылғанын көрсету
radius = 2  # Қаламның радиусы
color = 'blue'  # Түсті орнату
mode = 'pen'  # Қолданылатын құралды орнату

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Белгіленген өлшемдегі терезені құру
pygame.display.set_caption('Paint')  # Терезеге атау беру
clock = pygame.time.Clock()  # Уақытты басқару үшін
screen.fill(pygame.Color('white'))  # Экранды ақ түспен толтыру
font = pygame.font.SysFont('None', 60)  # Мәтінді көрсету үшін қаріпті жасау

def drawLine(screen, start, end, width, color): 
    # Бастапқы және соңғы нүктелердің x және y координаталарын алу
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    # x және y координаталарының абсолютті айырмашылықтарын есептеу
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    # Тікелей сызықтың теңдеуі үшін коэффициенттер
    A = y2 - y1  # Тікелей сызық бойынша
    B = x1 - x2  # Көлденең сызық бойынша
    C = x2
