import numpy as np

chan_counter = 0
for j in range(168):
    for i in range(16):
        print(f"%d " % (16*j + i),end='')
        chan_counter = chan_counter + 1
    print()
