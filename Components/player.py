import pygame


class Player:
    def __init__(self, screenWidth, screenHeight):
        self.playerSpeed = 10
        self.defaultSpeed = 10
        self.player = pygame.Rect(screenWidth-20, screenHeight/2-70, 10, 140)

    def getPlayer(self):
        return self.player

    def drawPlayer(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), self.player)

    def resetSpeed(self):
        self.playerSpeed = self.defaultSpeed

    def changeSpeed(self, speed):
        global playerSpeed
        playerSpeed = speed

    def moveUp(self):
        self.player.y -= self.playerSpeed
        if (self.player.top <= 0):
            self.player.y = 0

    def moveDown(self, screenheight):
        self.player.y += self.playerSpeed
        if (self.player.bottom > screenheight):
            self.player.bottom = screenheight
