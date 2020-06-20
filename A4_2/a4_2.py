# importing pygame
import pygame
from pygame.locals import * 
from sys import exit
import random
import time

# initializing the pygame environment 
pygame.init()

screen = pygame.display.set_mode((250,250))
pygame.display.set_caption('ITEC 4270')

# importing image
robot = pygame.image.load('robot.png').convert()
robot_rect = robot.get_rect()
robot_x = 10
robot_y = 10
robot_rect.center = (robot_x,robot_y)
screen.blit(robot,(robot_x,robot_y))
# creating the goal 

goal_x = random.randint(20,200)
goal_y = goal_x + 20
goal_h = 40
goal_w = 40
BLUE = (0,0,255)
goal_rect = pygame.Rect(goal_x,goal_y,goal_h,goal_w)



def move_robot():
    global robot_x
    global robot_y
    if robot_x < goal_x:
        robot_x = robot_x + 4
    if robot_y < goal_y:
        robot_y = robot_y + 4
    robot_rect.center = (robot_x,robot_y)
    screen.blit(robot,(robot_x,robot_y))

def display(message):
    font = pygame.font.Font(None,36) 
    text = font.render(message,1,(10,10,10))
    screen.blit(text,( 50,10))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255,255,255))    
    pygame.draw.rect(screen,BLUE,goal_rect)
    
    if(robot_rect.colliderect(goal_rect)):
        display("Reached Goal")
    
    move_robot()
    pygame.display.flip()
    pygame.display.update()
    time.sleep(.1)

pygame.display.update()

