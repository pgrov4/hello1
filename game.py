import pygame
import clock
import random
pygame.init()
black = (0,0,0)
white = (255,255,255)
display_width=800
display_height=600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carimg=pygame.image.load('racecar.png')

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    pygame.mixer.init()
    pygame.mixer.music.load("beatown15full.wav")
    pygame.mixer.music.play(-1,0.0)
    intro = True
    green=(0,200,0)
    red=(200,0,0)
    bright_red = (255, 0, 0)
    bright_green = (0, 255, 0)

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit)

        mouse = pygame.mouse.get_pos()

        # print(mouse)

        # if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        #     pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
        # else:
        #     pygame.draw.rect(gameDisplay, green, (150, 450, 100, 50))
        #     smallText = pygame.font.Font("freesansbold.ttf", 20)
        #     textSurf, textRect = text_objects("GO!", smallText)
        #     textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        #     gameDisplay.blit(textSurf, textRect)
        # pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))

        # pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        # pygame.draw.rect(gameDisplay, red,(550,450,100,50))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro= False






def car(x,y):
    gameDisplay.blit(carimg, (x,y))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

car_width = 73

def game_loop():

    x=display_width*0.45
    y=display_height*0.60
    x_change=0
    y_change=0
    crashed = False
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 1
    thing_width = 100
    thing_height = 100
    dodged=0
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
        gameDisplay.fill(white)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)


        if x > (display_width - car_width) or x < 0:
            crashed = True

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()


        #print(event)
        # gameDisplay.fill(white)
        # things(thing_startx, thing_starty, thing_width, thing_height, black)
        # thing_starty += thing_speed

        car(x,y)

        pygame.display.update()
    clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()