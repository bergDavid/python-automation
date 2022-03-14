import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            self.contents += [k] * int(v)

    def __str__(self):
        return str(self.contents)

    def draw(self, num):
        n = len(self.contents)
        if num >= n:
            return self.contents
        r = []
        for i in range(0, num):
            bid = random.randint(0, n - 1)
            r.append(self.contents.pop(bid))
            n -= 1

        return r

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for n in range(0, num_experiments):
        #create a dictionary of the collected balls
        hatcc = copy.deepcopy(hat)
        result = hatcc.draw(num_balls_drawn)
        collected = {}
        for ball in result:
            value = collected.get(ball,0)
            collected[ball] = value + 1
        
        foundmatch = True
        for ball, amount in expected_balls.items():
            if collected.get(ball,0) < amount:
                foundmatch = False
                break
              
        if foundmatch:
            m = m + 1
    return m/num_experiments