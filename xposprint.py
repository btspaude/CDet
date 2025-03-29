import numpy as np

chan_counter = 0
for j in range(12):
    for i in range(16):
        print(f"%0.2f " % ((((16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter = chan_counter + 1
    print("## ROC 63 Slot 3")

chan_counter2 = chan_counter
for j in range(12):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter2 = chan_counter2 + 1
    print("## ROC 63 Slot 4")

chan_counter3 = chan_counter2
for j in range(12):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter2 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter3 = chan_counter3 + 1
    print("## ROC 63 Slot 5")

chan_counter4 = chan_counter3
for j in range(12):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter3 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter4 = chan_counter4 + 1
    print("## ROC 63 Slot 6")

chan_counter5 = chan_counter4
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter4 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter5 = chan_counter5 + 1
    print("## ROC 63 Slot 7")

chan_counter6 = chan_counter5
for j in range(12):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter5 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter6 = chan_counter6 + 1
    print("## ROC 63 Slot 8")

chan_counter7 = chan_counter6
for j in range(12):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter6 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter7 = chan_counter7 + 1
    print("## ROC 63 Slot 9")

chan_counter8 = chan_counter7
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter7 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter8 = chan_counter8 + 1
    print("## ROC 63 Slot 10")

chan_counter9 = chan_counter8
for j in range(6):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter8 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter9 = chan_counter9 + 1
    print("## ROC 63 Slot 10")

chan_counter10 = chan_counter9 + 96
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter9 + 96 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter10 = chan_counter10 + 1
    print("## ROC 63 Slot 13")

chan_counter11 = chan_counter10 + 128
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter10 + 128 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter11 = chan_counter11 + 1
    print("## ROC 63 Slot 14")

chan_counter12 = chan_counter9
for j in range(6):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter9 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter12 = chan_counter12 + 1
    print("## ROC 63 Slot 14")

chan_counter13 = chan_counter10
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter10 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter13 = chan_counter13 + 1
    print("## ROC 63 Slot 15")

chan_counter14 = chan_counter11
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter11 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter14 = chan_counter14 + 1
    print("## ROC 63 Slot 16")

chan_counter15 = chan_counter14 + 128
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter14 + 128 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter15 = chan_counter15 + 1
    print("## ROC 63 Slot 16")

chan_counter16 = chan_counter14
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter14 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter16 = chan_counter16 + 1
    print("## ROC 63 Slot 17")

chan_counter17 = chan_counter16 + 192
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter16 + 192 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter17 = chan_counter17 + 1
    print("## ROC 63 Slot 17")

chan_counter18 = chan_counter15
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter15 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter18 = chan_counter18 + 1
    print("## ROC 63 Slot 18")

chan_counter19 = chan_counter18 + 192
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter18 + 192 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter19 = chan_counter19 + 1
    print("## ROC 63 Slot 18")

chan_counter20 = chan_counter18 + 64
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter18 + 64 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter20 = chan_counter20 + 1
    print("## ROC 63 Slot 19")

chan_counter21 = chan_counter20 + 192
for j in range(4):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter20 + 192 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter21 = chan_counter21 + 1
    print("## ROC 63 Slot 19")

chan_counter22 = chan_counter19
for j in range(8):
    for i in range(16):
        print(f"%0.2f " % ((((chan_counter19 + 16*j + i)//672)%2)*0.50-0.25),end='')
        chan_counter22 = chan_counter22 + 1
    print("## ROC 63 Slot 13")

