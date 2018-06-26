import pygame
import clock

pygame.init()
black = (0,0,0)
white = (255,255,255)
display_width=800
display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

carimg=pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carimg, (x,y))

car_width = 73
def game_loop():
    x=display_width*0.45
    y=display_height*0.60
    x_change=0
    y_change=0
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                elif event.key == pygame.K_RIGHT:
                    x_change = 1
                elif event.key == pygame.K_UP:
                    y_change = -1
                elif event.key == pygame.K_DOWN:
                    y_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change=0

        x += x_change
        y += y_change
        if x > (display_width - car_width) or x < 0:
            crashed = True

        print(event)
        gameDisplay.fill(white)
        car(x,y)

        pygame.display.update()
    #clock.tick(60)
game_loop()
pygame.quit()
quit()