# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator

hat1 = prob_calculator.Hat(red=3, blue=2, green=6)
probability = prob_calculator.experiment(hat=hat1,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(str(probability))