#! /usr/bin/env python3

import time
import logging
from random import randint
from timeit import default_timer as timer

logger = logging.getLogger('machine_coffee')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler(filename='machine.log', encoding='UTF-8')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('(%(name)s)%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def log(func):
    def func_wrapper(*args, **kwargs):
        title = [str(x).capitalize() for x in func.__name__.split('_')]
        title = ' '.join(title)
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        t = end - start
        if t < 1:
            t = f'{t * 1000:.3f} ms'
        else:
            t = f'{t:.3f} s '
        logger.info(f'Running: {title:15} [ exec-time = {t} ]')
        return result
    return func_wrapper


class CoffeeMachine:

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)