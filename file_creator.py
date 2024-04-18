import numpy as np
import os
import random
from string import ascii_letters
list_possible_letters = [letter for letter in ascii_letters]
list_possible_letters.append("\n")
list_possible_letters.append(" ")


tmp = np.random.normal(0, 10, 30)

list_file_size = [(1000000, 1000, 10), (21, 5, 6400), (150, 15, 100), (501, 5, 1000), (1000, 100, 500), (5000, 100, 300), (10000, 100, 200)]

for file_info in list_file_size:
    mean = file_info[0]  * 1000 # 1000 byte -> 1 kb
    std = file_info[1] * 1000 # 1000 byte -> 1 kb
    number_file = file_info[2]
    if not os.path.exists(str(mean)):
        os.mkdir(str(mean))

    size_file = np.random.normal(mean, std, number_file)
    cmpt = 0
    for size in size_file:
        f = open(str(mean)+"/"+str(cmpt)+".txt", 'w')
        for i in range(int(size)):
            f.write(random.choice(list_possible_letters))
        f.close()
        cmpt += 1
