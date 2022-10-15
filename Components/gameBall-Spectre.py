import pygame
import random
import mods
import Components.ball as ball
import Components.sounds as sounds

# Gets reference to functions in mods.py and puts them in a list
filterModFunctions = filter(lambda x: "_" not in "mods." + x[0], dir(mods))
modList = list(filterModFunctions)

print(modList)


class GameBall(ball.Ball):
    def __init__(self, screen):
        self.ball = pygame.Rect(
            screen.get_width() / 2 - 15, screen.get_height() / 2 - 15, 30, 30
        )
        self.ballSpeedX = 7
        self.ballSpeedY = 7
        self.maxX = screen.get_width()
        self.maxY = screen.get_height()
        self.color = (200, 200, 200)
        self.screen = screen

    def getBallDirection(self):
        if self.ballSpeedX > 0:
            return True
        return False

    def resetBall(self):
        self.ball.x = self.maxX / 2 - 15
        self.ball.y = self.maxY / 2 - 15
        self.ballSpeedX *= random.choice((1, -1))
        self.ballSpeedY *= random.choice((1, -1))

    # Overrides the parent ball method
    def moveBall(self, player, opponent, itemBox, score):
        self.ball.x += self.ballSpeedX
        self.ball.y += self.ballSpeedY

        # Ball Collision with top and bottom of screen
        if self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height():
            self.ballSpeedY *= -1

        # Reaching the left side of the screen
        if self.ball.left <= 0:
            sounds.playScoreSound()
            self.resetBall()
            player.resetCharacter()
            opponent.resetCharacter()
            score.increase_player_score()

        # Reaching the right side of the screen
        if self.ball.right >= self.screen.get_width():
            sounds.playScoreSound()
            self.resetBall()
            player.resetCharacter()
            opponent.resetCharacter()
            score.increase_opponent_score()

        # Bounce off player
        if self.ball.colliderect(player.getCharacter()):
            sounds.playPongSound()
            self.ballSpeedX *= -1
            if self.ball.y > player.getCharacter().centery + 20:
                self.ballSpeedY = abs(self.ballSpeedY)
            elif self.ball.y < player.getCharacter().centery - 20:
                self.ballSpeedY = -abs(self.ballSpeedY)

        # Bounce off opponent
        if self.ball.colliderect(opponent.getCharacter()):
            sounds.playPongSound()
            self.ballSpeedX *= -1
            if self.ball.y > opponent.getCharacter().centery + 20:
                self.ballSpeedY = abs(self.ballSpeedY)
            elif self.ball.y < opponent.getCharacter().centery - 20:
                self.ballSpeedY = -abs(self.ballSpeedY)

        if self.ball.colliderect(itemBox.getBox()):
            # random.choice(modList)(player, opponent, self)
            f"mods.{modList[random.randrange(0, modList.length()-1])(player, opponent, self)}"
            itemBox.removeBox()
