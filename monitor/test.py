import random
import time
import matplotlib as mpl
import numpy as np
mpl.use('Agg')
from matplotlib import pyplot as plt

from main import plot


def gen():
    while True:
        yield random.random() * 18 + 12, 512 + random.randint(1, 512)
        time.sleep(2)

for x in plot(gen()):
    print('pic')
    pass
