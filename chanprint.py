import numpy as np

chan_counter = 0
slot_20_counter = 2688
for j in range(168):
    if (int(j/42)==0 or int(j/42)==2):
        for i in range(16):
            print(f"%d " % (16*j + i),end='')
            chan_counter = chan_counter + 1
    else:
        for i in range(16):
            print(f"%d " % (16*j + 15 - i),end='')
            chan_counter = chan_counter + 1
    print()
    if j==41 or j==83 or j==125 or j==167:
        print("#")
        for i in range(3):
            for k in range(16):
                print(f"%d " % (k + slot_20_counter),end='')
                chan_counter = chan_counter + 1
            slot_20_counter += 16
            print()
        print("#")


