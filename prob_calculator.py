import copy
import random


# Consider using the modules imported above.

class Hat:
    contents = []

    def __init__(self, **balls):
        for name, quantity in balls.items():
            for i in range(quantity):
                self.contents.append(name)

    def __str__(self):
        return f'Hat\nContents: {self.contents}'

    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            return self.contents
        contents = copy.copy(self.contents)
        contents_draw = []
        for i in range(num_balls_drawn):
            random_index = random.randint(0, len(contents) - 1)
            contents_draw.append(contents.pop(random_index))
        return contents_draw

    def get_contents(self):
        return self.contents


def is_successful_experiment(actual, expected):
    for k, v in expected.items():
        if actual.count(k) < v:
            return False
    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for i in range(num_experiments):
        if is_successful_experiment(hat.draw(num_balls_drawn), expected_balls):
            successful_experiments += 1
    return successful_experiments / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=20)
