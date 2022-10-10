import pygame


class Ball:
    def getBall(self):
        return self.ball

    def drawBall(self):
        pygame.draw.ellipse(self.screen, (200, 200, 200), self.ball)

    def moveBall(self):
        self.ball.x += self.ballSpeedX
        self.ball.y += self.ballSpeedY

        # Ball Collision with top and bottom of screen
        if (self.ball.top <= 0 or self.ball.bottom >= self.screen.get_height()):
            self.ballSpeedY *= -1

        # Ball Collision with left and right of screen
        if (self.ball.left <= 0 or self.ball.right >= self.screen.get_width()):
            self.ball.removeBall()


""" 
def ballMovement():
    global ballSpeedX, ballSpeedY, playerScore, opponentScore
    pygame.draw.ellipse(screen, lightGrey, ball)
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Bounce off top and bottom
    if (ball.top <= 0 or ball.bottom >= screenHeight):
        ballSpeedY *= -1

    # Bounce off left and right
    if (ball.left <= 0):
        sounds.playScoreSound()
        ballRestart()
        player.resetHeight()
        op.resetHeight()
        score.increase_player_score()

    if (ball.right >= screenWidth):
        sounds.playScoreSound()
        ballRestart()
        player.resetHeight()
        op.resetHeight()
        score.increase_opponent_score()

    # Bounce off player
    if (ball.colliderect(player.getPlayer())):
        sounds.playPongSound()
        ballSpeedX *= -1
        if (ball.y == player.getPlayer().centery):
            ballSpeedY = 0
        elif (ball.y > player.getPlayer().centery + 20):
            ballSpeedY = abs(ballSpeedY)
        elif (ball.y < player.getPlayer().centery - 20):
            ballSpeedY = -abs(ballSpeedY)

    # Bounce off opponent
    if (ball.colliderect(op.getOpponent())):
        sounds.playPongSound()
        ballSpeedX *= -1
        if (ball.y > op.getOpponent().centery + 20):
            ballSpeedY = abs(ballSpeedY)
        elif (ball.y < op.getOpponent().centery - 20):
            ballSpeedY = -abs(ballSpeedY)

    # Collision with item box
    if ball.colliderect(box.getBox()):
        sounds.playAlienSound()
        box.removeBox()
        if (ballSpeedX < 0):
            op.changeHeight(-paddleShrink.shrinkPaddle(op.getOpponent().height))
        else:
            player.changeHeight(-paddleShrink.shrinkPaddle(player.getPlayer().height)) """
