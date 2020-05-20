import numpy as np 
import random
import Pong





class AI(object):
    def __init__(self, Ball, Player, maxX, maxY):
        self.p = Player
        self.b = Ball

        self.stateSpace = [i for i in range(maxY)]

        self.actionSpace = {'U': -Pong.AI_SPEED, 'D': +Pong.AI_SPEED}
        self.actionList = ['U', 'D']

    def getPos(self):
        return self.p.rect.y
    
    def outOfBounds(self, newState):
        if newState > 425:
            return True
        if newState < 0:
            return True
        
        return False
    
    def AI_win(self):

        if Pong.player2.getScore() > Pong.MAX_SCORE:
            return True
        
        return False


    def step(self, action):
        resultState = self.getPos() + self.actionSpace[action]

        #TODO figure out how to set rewards
        reward = -1 if not self.AI_win() else 0

        #TODO return info correctly
        if not self.outOfBounds(resultState):
            self.p.rect.y += self.actionSpace[action]
            return resultState, reward, self.AI_win(), None
        else:
            return self.getPos(), reward, self.AI_win(), None


    #TODO discuss resetting the environment





            