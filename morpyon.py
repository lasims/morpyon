#! /usr/bin/env python

from sys import exit
import pygame

screen_size = (640, 400)
red = (255, 0, 0)
blue = (0, 0, 255)
grey = (64, 64, 64)
position = (10, 10)
size = (20, 20)

screen = pygame.display.set_mode(screen_size)

screen.fill(grey)

case1 = pygame.Rect(position, size)
case1surface = screen.subsurface(case1)
case1surface.fill(red)

pygame.display.update()
while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit(0)



