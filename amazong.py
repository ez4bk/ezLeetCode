def getMinSize(gameSize, k):
    gameSize.sort()
    if gameSize[-1] > gameSize[0] + gameSize[-2]:
        return gameSize[-1]
    
    bfGameSize = gameSize[-1]
    
    left, right = 0, len(gameSize) - 2
    while left < right:
        if (gameSize[left] + gameSize[right]) < bfGameSize:
            left += 1
        else:
            right -= 1
    return gameSize[left] + gameSize[right]