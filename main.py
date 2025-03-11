#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module
import random

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_text(screen, text, font, font_color, position, anti_aliased=True, italic=False, bold=False):
    img = font.render(text, True, font_color)
    screen.blit(img, position,)

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()
    
    
    x1 =random.randrange(1,600)
    x2 =random.randrange(1,600)
    x3 =random.randrange(1,600)
    x4 =random.randrange(1,600)
    x5 =random.randrange(1,600)

    y1 =random.randrange(1,400)
    y2 = random.randrange(1,400)
    y3 =random.randrange(1,400)
    y4 =random.randrange(1,400)
    y5 =random.randrange(1,400)

    size1= int(random.randrange(10,100))
    size2= int(random.randrange(10,100))
    size3= int(random.randrange(10,100))

    free = pygame.font.SysFont('airal',size1)
    dot = pygame.font.Font('Doto-VariableFont_ROND,wght.ttf',size2)
    lib = pygame.font.Font('LiberationMono-Italic.ttf',size3)
    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        


        draw_text(screen, 'hello',free, config.RED,(x1,y1))
        draw_text(screen, 'welcome to the game',dot, config.BLACK,(x2,y2))
        draw_text(screen, 'random thing',free, config.PURPLE,(x3,y3))
        draw_text(screen, 'you lossed',dot, config.BLUE,(x4,y4))
        draw_text(screen, 'you win',lib, config.GREEN,(x5,y5))



        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
