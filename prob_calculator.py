import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls) -> None:
        self.contents=[]
        self.balls =balls
        for k,v in balls.items():
            for i in range(v):
                self.contents.append(k)
    def draw(self,numberOfBalls):
            self.drawnBalls=[]
            for i in range(min(numberOfBalls,len(self.contents))):
                temp=random.choice(range(len(self.contents)))
                self.drawnBalls.append(str(self.contents[temp]))
                self.contents.pop(temp)
            return self.drawnBalls
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successfulExperiments=0
    for j in range(num_experiments):
        expBalls=copy.deepcopy(expected_balls)
        hat1=copy.deepcopy(hat)
        drwanBalls=dict()
        balls_drawn=hat1.draw(num_balls_drawn)
        for i in balls_drawn:
            drwanBalls[i]=drwanBalls.get(i,0) + 1
        flag=1
        for k,v in expBalls.items():  
            if k in drwanBalls:
                if drwanBalls[k]>=v:
                    flag=1
                else:
                    flag=0
                    break                        
            else:
                flag=0
                break        
        if flag==1:
            successfulExperiments+=1
    return successfulExperiments/num_experiments