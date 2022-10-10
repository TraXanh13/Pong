import pygame


class Character:

    def getCharacter(self):
        return self.character

    def drawCharacter(self):
        pygame.draw.rect(self.screen, (200, 200, 200), self.character)

    def resetSpeed(self):
        self.speed = self.defaultSpeed

    def resetHeight(self):
        self.character.inflate_ip(0, 140-self.character.height)

    def resetCharacter(self):
        self.character.inflate_ip(0, 140-self.character.height)
        self.speed = self.defaultSpeed

    def changeSpeed(self, speed):
        self.speed = speed

    def changeHeight(self, height):
        self.character.inflate_ip(0, height)
