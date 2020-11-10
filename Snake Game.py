# -*- coding: utf-8 -*-
"""
Created on Weds Nov 4 08:53:46 2020

@author: 612683226
"""

import pygame
import time
import random
import sys
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Welcome to my Snake game by Craig')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("gabriola", 25)
score_font = pygame.font.SysFont("georgia", 40)
 
Length_of_snake = 1
 
def Main_menu():
    global Length_of_snake
    menu=True
    selected="start"
 
    while menu:
        dis.fill(blue)
        message("Press y to play again OR n to quit", red)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    game_over = True
                    game_close = False
                    selected = "quit"
                if event.key == pygame.K_y:
                    selected = "start"
                    menu=False
                    
        if selected == "quit":
            pygame.quit()
            sys.exit()
        elif selected == "start" and menu == False:    
            gameLoop()
        else:
            time.sleep(10)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message_lost(msg, color):
    mesg = score_font.render(msg, True, red)
    dis.blit(mesg, [dis_width / 2.6, dis_height / 4])
    
def message(msg, color):
    mesg = font_style.render(msg, True, black)
    dis.blit(mesg, [dis_width / 3.2, dis_height / 2])
 
 
def gameLoop():
    global Length_of_snake
    game_over = False
    game_close = False

 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message_lost("You Lost!", red)
            Main_menu()
#            time.sleep(3)
#            dis.fill(blue)
            
#            time.sleep(10)
            
#            if event == False:
#               game_over(true)
#                game_close(false)
#            else:
#                print("test")
                                                    
             
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
        x1 += x1_change
        y1 += y1_change
        dis.fill(red)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                dis.fill(blue)
                message_lost("You Lost!", red)
                time.sleep(3)
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
#gameLoop()
Main_menu()