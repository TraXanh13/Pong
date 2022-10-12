from random import random
import pygame


class Ball:
    def getBall(self):
        return self.ball

    def drawBall(self):
        pygame.draw.ellipse(self.screen, (200, 200, 200), self.ball)

    def moveBall(self):
        self.ball.x += self.ballSpeedX
        self.ball.y += self.ballSpeedY

        # Bounce off top and bottom
        if (self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height()):
            self.ballSpeedY *= -1
