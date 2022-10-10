import pygame


class Opponent:
    def __init__(self, screenWidth, screenHeight):
        self.opponentSpeed = 10
        self.defaultSpeed = 10
        self.opponent = pygame.Rect(
            20, screenHeight/2-70, 10, 140)

    def getOpponent(self):
        return self.opponent

    def drawOpponent(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.opponent)

    def resetSpeed(self):
        self.opponentSpeed = self.defaultSpeed

    def changeSpeed(self, speed):
        self.opponentSpeed = speed

    def resetHeight(self):
        self.opponent.inflate_ip(0, 140-self.opponent.height)

    def changeHeight(self, height):
        self.opponent.inflate_ip(0, height)

    # Moves the opponent to follow the ball
    def moveOpponent(self, ball, screenHeight,):
        if ball.y > self.opponent.y:
            self.opponent.y += self.opponentSpeed
            if self.opponent.bottom >= screenHeight:
                self.opponent.bottom = screenHeight
        if ball.y < self.opponent.y:
            self.opponent.y -= self.opponentSpeed
            if self.opponent.top <= 0:
                self.opponent.top = 0
