import pygame

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 512)

# Sound variables (Supports wav and ogg files)
pongSound = pygame.mixer.Sound('./media/pong.ogg')
scoreSound = pygame.mixer.Sound('./media/score.ogg')

def play_pong_sound():
    pygame.mixer.Sound.play(pongSound)

def play_score_sound():
    pygame.mixer.Sound.play(scoreSound)