import pygame
import Components.ball as ball
import random
import Components.sounds as sounds
import Components.itemBox as box
import Mods.paddleShrink as paddleShrink


class GameBall(ball.Ball):
    def __init__(self, screen):
        self.ball = pygame.Rect(screen.get_width()/2-15,
                                screen.get_height()/2-15, 30, 30)
        self.ballSpeedX = 10
        self.ballSpeedY = 10
        self.maxX = screen.get_width()
        self.maxY = screen.get_height()
        self.screen = screen

    def resetBall(self):
        self.ball.x = self.maxX/2-15
        self.ball.y = self.maxY/2-15
        self.ballSpeedX *= random.choice((1, -1))
        self.ballSpeedY *= random.choice((1, -1))

    def changeBallSpeed(self, speed):
        self.ballSpeedX = speed + random.randint(-10, 10)
        self.ballSpeedY = speed + random.randint(-10, 10)
