#! /usr/bin/env python

from sys import exit
import pygame

pygame.display.set_mode((640, 400))

while 1:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit(0)
