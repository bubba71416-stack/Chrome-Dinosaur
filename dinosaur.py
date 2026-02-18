import pygame
from pygame.locals import *
import sys

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

dino = Dinosaur(HEIGHT)

running = True
while running:
    deltaTime = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                dino.jump()
