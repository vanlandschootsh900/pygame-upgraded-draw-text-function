#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module


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

# def welcome_text(screen, text, font, size, text_color, x,y, bold=True):
#     welcome = font.render(text, True, text_color, size)
#     screen.blit(welcome, (x,y), bold)

def draw_text(screen, text, font, text_color, x,y, bold= True):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))



def main():
    
    screen = init_game()
    clock = pygame.time.Clock()
    

    red= config.RED
    purple= config.PURPLE
    black= config.BLACK
    green= config.GREEN

    size_normale= 40
    size_big= 60
    small_size=30
    free = 'freemono.ttf'
    
    
    
    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        


        draw_text(screen, 'hello',free,40, config.PURPLE,400,440)




        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
