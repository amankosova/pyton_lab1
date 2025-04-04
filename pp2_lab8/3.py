import pygame 
 
WIDTH, HEIGHT = 1200, 800 
FPS = 90      #экранның жаңару жиілігі
draw = False   #Бұл айнымалы экранда сурет салынатынын анықтайды          
radius = 4    #щетка радиусы
color = 'lime'           
mode = 'pen'                
 
pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT]) 
pygame.display.set_caption('Painter') 
clock = pygame.time.Clock() # уақытты басқару үшін 
screen.fill(pygame.Color('white'))  #Экранды толығымен ақ түспен толтырады
font = pygame.font.SysFont('None', 60)
 
 
def drawLine(screen, start, end, width, color):
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    # айырмашылықты есептейді
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    # коэф. Ax + By + C = 0
    A = y2 - y1  # вертикально
    B = x1 - x2  # горизонтально
    C = x2 * y1 - x1 * y2  # сызықтың тұрақты мүшесі
    
    # If the line is more horizontal than vertical
    if dx > dy: 
        # Ensure x1 is to the left of x2
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        #  сызықтың бағытын дұрыс орнату үшін координаталар орын ауыстырылады
# сызықтың әрбір x координаты үшін сәйкес келетін y координатын есептейді және экранға пиксель салады
        for x in range(x1, x2): 
            y = (-C - A * x) / B 
            # Draw a circle (pixel) at (x, y) position
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    # If the line is more vertical than horizontal
    else: 
        # Ensure y1 is below y2
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # Iterate over y coordinates
        for y in range(y1, y2): 
            # Calculate x coordinate using the line equation
            x = (-C - B * y) / A 
            # Draw a circle (pixel) at (x, y) position
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

 
 
def drawCircle(screen, start, end, width, color): 
    # Extract x and y coordinates of start and end points
    x1 = start[0]  
    x2 = end[0]  
    y1 = start[1]  
    y2 = end[1]  
    
    # шенбер центрин есептеу
    x = (x1 + x2) / 2  # х бойынша
    y = (y1 + y2) / 2  # у бойынша
    
    #шенбер радиусы
    radius = abs(x1 - x2) / 2 
    
    # позицияга шенбер салу
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width) 
 
 
def drawRectangle(screen, start, end, width, color): 
    x1 = start[0]  
    x2 = end[0]  
    y1 = start[1]  
    y2 = end[1] 
    
    widthr = abs(x1 - x2)  # енин есептеу
    height = abs(y1 - y2)  # бииктигин есептеу
    
    # Бастапқы және соңғы нүктелердің орналасуына қарай экранға тіктөртбұрыш салу
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width) 

     
def drawSquare(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    mn = min(abs(x2 - x1), abs(y2 - y1)) 
 
 
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn)) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn)) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn)) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn)) 
 
def drawRightTriangle(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
     
    if x2 > x1 and y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
 
 
def drawEquilateralTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
 #Үшбұрыштың негізі мен биіктігін есептеу үшін формулалар қолданылады
    width_b = abs(x2 - x1) #үшбұрыштың негізі
    height = (3**0.5) * width_b / 2 # үшбұрыштың биіктігі
 
    if y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width) 
    else: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height))) 
     
 
def drawRhombus(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) 
 
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()  #терезе жабылады
         
        if event.type == pygame.KEYDOWN: 
            
            if event.key == pygame.K_r: 
                mode = 'rectangle'  #  draw rectangles
            if event.key == pygame.K_c: 
                mode = 'circle'  # draw circles
            if event.key == pygame.K_p: 
                mode = 'pen'  #  use a pen
            if event.key == pygame.K_e: 
                mode = 'erase'  #  erase
            if event.key == pygame.K_s: 
                mode = 'square'  #  draw squares
            if event.key == pygame.K_q: 
                screen.fill(pygame.Color('white'))  # Clear the screen by filling it with white color
 
            # Change the color based on the pressed key
            if event.key == pygame.K_1: 
                color = 'black'  #  black
            if event.key == pygame.K_2: 
                color = 'green'  #o green
            if event.key == pygame.K_3: 
                color = 'red'  #  red
            if event.key == pygame.K_4: 
                color = 'blue'  #  blue
            if event.key == pygame.K_5: 
                color = 'yellow'  #  yellow
            if event.key == pygame.K_t: 
                mode = 'right_tri'  #  draw right triangles
            if event.key == pygame.K_u: 
                mode = 'eq_tri'  #  draw equilateral triangles
            if event.key == pygame.K_h: 
                mode = 'rhombus'  #  draw rhombuses
   
 
      
        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  # Enable drawing
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Draw a circle (pixel) if the pen mode is active
            prevPos = event.pos  # Бастапқы орын ретінде тышқанның орын ауыстыруын сақтаймыз.



 
        
        if event.type == pygame.MOUSEBUTTONUP:  
        # When the mouse button is released
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, radius, color)  # Draw a rectangle if the mode is set to draw rectangles
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, radius, color)  # Draw a circle if the mode is set to draw circles
            elif mode == 'square': 
                drawSquare(screen, prevPos, event.pos, color)  # Draw a square if the mode is set to draw squares
            elif mode == 'right_tri': 
                drawRightTriangle(screen, prevPos, event.pos, color)  # Draw a right triangle if the mode is set to draw right triangles
            elif mode == 'eq_tri': 
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)  # Draw an equilateral triangle if the mode is set to draw equilateral triangles
            elif mode == 'rhombus': 
                drawRhombus(screen, prevPos, event.pos, radius, color)  # Draw a rhombus if the mode is set to draw rhombuses
            draw = False  # Disable drawing

 
       
        if event.type == pygame.MOUSEMOTION:  
        # When the mouse is moved
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color)  # If drawing is enabled and pen mode is active, draw a line between the last position and the current position
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')  # If drawing is enabled and erase mode is active, draw a white line (erase) between the last position and the current position
            lastPos = event.pos  # Әр қозғалыста соңғы орынды жаңартып отыру үшін.
 

    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))  # Экранның жоғарғы бұрышында радиус мәнін көрсету үшін ақ түсті төртбұрыш салынған.
    renderRadius = font.render(str(radius), True, pygame.Color(color))  # Қазіргі радиус мәнін текст ретінде өңдеу.


    screen.blit(renderRadius, (1120, 5))  #Текстті экранға белгілі бір орынға (1120, 5) орналастыру.
 
    pygame.display.flip()  # дисплей жанартады
    clock.tick(FPS)  # Экран жаңаруының жиілігін бақылау