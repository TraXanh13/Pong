def shrinkPaddle(paddleSize):
    if(paddleSize > 50):
        return int(paddleSize * .75)

    return paddleSize