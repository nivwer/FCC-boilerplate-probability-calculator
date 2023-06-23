import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      c = (f"{key}," * value).split(",")
      c.pop(-1)
      self.contents.extend(c)
    print(self.contents)

  def draw(self, number):
    r_contents = []
    if number > len(self.contents): return self.contents
    for i in range(number):
      r = self.contents.pop(int(random.random() * len(self.contents)))
      r_contents.append(r)
    return r_contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for n in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    colors = hat_copy.draw(num_balls_drawn)
    for v in expected_balls.keys():
      n = 0
      for x in range(len(colors)):
        if colors[x] == v: n += 1
      if n < expected_balls[v]:
        count += 1
        break
  return 1 - count / num_experiments
