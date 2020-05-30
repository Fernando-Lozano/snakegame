import pygame
import time
import random

# initializing game
pygame.init()

crash_sound = pygame.mixer.Sound("/Users/ferna/Documents/snakegame/crash.wav")
yum_sound = pygame.mixer.Sound("/Users/ferna/Documents/snakegame/yum.wav")
pygame.mixer.music.load("/Users/ferna/Documents/snakegame/jazz.wav")

# colors

white = (246, 174, 45)
yellow = (246, 174, 45)
black = (0, 0, 0)
red = (242, 100, 25)
green = (85, 221, 224)
blue = (51, 101, 138)

# setting simple variables
dis_width = 800
dis_height = 500

# display stuff
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Fernando K Lozano')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# fonts
font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
  value = score_font.render("Your Score: " + str(score), True, yellow)
  dis.blit(value, [50, 50])

def our_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) 

def message1(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 2]) 

def gameLoop():  # creating a function
    game_over = False
    game_close = False
    pygame.mixer.music.play(-1)
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost!", red)
            message1("Press Q to Quit or C to Play Again", red)
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > length_of_snake:
          del snake_list[0]

        for x in snake_list[:-1]:
          if x == snake_Head:
            game_close = True
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        
        pygame.display.update()

        

        if x1 == foodx and y1 == foody:
          foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
          foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
          length_of_snake += 1
          pygame.mixer.Sound.play(yum_sound)
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()