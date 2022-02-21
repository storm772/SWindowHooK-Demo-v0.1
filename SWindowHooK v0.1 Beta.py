import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((510, 100))
screen.fill((255,255,255))

font = pygame.font.SysFont("Arial", 32)
font2 = pygame.font.SysFont(None, 32)
def renderText(text, *pos):
    if not (pos): pos = (100,100)
    testE = font.render(text, True, (0))
    screen.blit(testE, (pos))

renderText('Input-Box:', (5,10))
renderText('Button:', (400, 10))

x2, y2, w2, h2 = 400, 50, 100, 32
borderRect = pygame.Rect(x2-3, y2-3, w2+6, h2+6)
buttonRect = pygame.Rect(x2, y2, w2, h2)

def drawButton():
    pygame.draw.rect(screen, (0,0,0), borderRect)
    pygame.draw.rect(screen, (200, 200, 200), buttonRect)

def renderButton(text):
    drawButton()
    screen.blit(font2.render(text, True, (0,0,0)), (buttonRect.centerx-35, buttonRect.centery-10))

x,y,w,h = 10,50,300,32
inputBoxBorderRect = pygame.Rect(x-3, y-3, w+6, h+6)
inputBoxRect = pygame.Rect(x, y, w, h)

color = pygame.Color('chartreuse4')

user_text = 'Input-Box!'
active = False

# Input Box inputs
def commands():
    print(user_text)

# Button inputs
def onClick():
    print(user_text)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonRect.collidepoint(event.pos): 
                active = True 
                onClick()
                active = False
            
            if inputBoxRect.collidepoint(event.pos): 
                if active == True:
                    pass
                else:
                    pass
                    active = True
            else: 
                if active == False:
                    pass 
                else:
                    pass
                    active = False

        if event.type == pygame.KEYDOWN:           
            if active == True:
                if event.key == pygame.K_RETURN: 
                    if not user_text:
                        pass
                    else:
                        commands()
                        user_text = ''
                        active = False
                if event.key == pygame.K_BACKSPACE: 
                    user_text = user_text[:-1]
                else: user_text += event.unicode
            else: 
                pass

    if (active == False):
        color = pygame.Color('chartreuse4')
    if (active == True):
        color = pygame.Color(53, 107, 0)

    pygame.draw.rect(screen, (0,0,0), inputBoxBorderRect)
    pygame.draw.rect(screen, color, inputBoxRect)
    renderButton('Button')
    
    screen.blit(font2.render(user_text, True, (255, 255, 255)), (inputBoxRect.x+5, inputBoxRect.y+5))

    pygame.display.update()
    pygame.time.Clock().tick(60)
