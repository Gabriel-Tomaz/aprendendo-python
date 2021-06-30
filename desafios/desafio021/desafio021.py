# =========Desafio 21==========
# Reproduzindo som com python

import pygame

pygame.init()
pygame.mixer.music.load('j.mp3')
pygame.mixer.music.play()
pygame.event.wait()