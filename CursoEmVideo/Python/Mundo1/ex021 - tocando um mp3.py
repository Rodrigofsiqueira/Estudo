import pygame

pygame.init()
pygame.mixer.music.load("trombone.mp3")
pygame.mixer.music.play()
pygame.event.wait()
