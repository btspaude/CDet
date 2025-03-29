import numpy as np

# Read arrays for module number, PMT number, and pixel number
# from single CSV file

# Read in the data from the CSV file
data = np.genfromtxt('unusedPixels_parsed.csv',
                     delimiter=',', skip_header=1)

# Get the number of rows and columns in the data
rows, cols = data.shape

# Initialize the channel counter
chan_counter = 0

NumPaddles = 16
NumBars = 14
NumSides = 2
NumLayers = 2
NumModules = 3

NumPaddlesPerSide = NumBars*(NumPaddles-2)*NumModules
xthickness = 0.005
xoffset = -1.0*xthickness*NumPaddlesPerSide/2.0

yleft = 0.25
yright = -0.25
yoffset = 0.10

zpos1 = 8.50 - 0.20 - 0.05
zpos2 = 8.50 - 0.20 + 0.05

# Print the xpos values for the CDET

missingcounter = 0
print("earm.cdet.xpos = ")
for layer in range(NumLayers):
    for side in range(NumSides):
        #print("Missing Pixels = ", missingcounter)
        missingcounter = 0
        for module in range(NumModules):
            localmodule = module + NumModules*layer
            for bar in range(NumBars):
                for paddle in range(NumPaddles):
                    # Search for the rows that match the current module, and PMT number
                    module_rows = data[np.where(data[:,0] == localmodule+1)]
                    flag = False
                    for row in module_rows:
                        if row[1] == side+1:
                            if row[2] == bar+1:
                                if row[3] == paddle+1:
                                    #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                    xpos = 999.0
                                    missingcounter = missingcounter + 1
                                    flag = True

                    if (not flag):
                        paddlenumber = (bar + NumBars*module)*NumPaddles + paddle
                        sectionoffset = (2*layer + side)*NumPaddlesPerSide
                        #if (xpos == 999.0):
                        #    print(f"***{paddlenumber + sectionoffset}***",end='')
                        xpos = xoffset + xthickness*paddlenumber - xthickness*missingcounter



                    # print xpos, with no newline
                    print(f"{xpos:.3f} ",end='')

                print()

print()
print("earm.cdet.ypos = ")
for layer in range(NumLayers):
    for side in range(NumSides):
        for module in range(NumModules):
            #print(f"Layer {layer} Side {side} Module {module}")
            localmodule = module + NumModules*layer
            for bar in range(NumBars):
                ypos = 10.0
                for paddle in range(NumPaddles):
                    if (module == 0):
                        if (bar <= NumBars/2):
                            if side == 0:
                                ypos = yleft-yoffset
                            else:
                                ypos = yright-yoffset
                        else:
                            if side == 0:
                                ypos = yleft
                            else:
                                ypos = yright

                    if module == 1:
                        if side == 0:
                            ypos = yleft+yoffset
                        else:
                            ypos = yright+yoffset

                    if (module == 2):
                        if (bar <= NumBars/2):
                            if side == 0:
                                ypos = yleft
                            else:
                                ypos = yright
                        else:
                            if side == 0:
                                ypos = yleft-yoffset
                            else:
                                ypos = yright-yoffset

                    # Search for the rows that match the current module, and PMT number
                    module_rows = data[np.where(data[:,0] == localmodule+1)]
                    for row in module_rows:
                        if row[1] == side+1:
                            if row[2] == bar+1:
                                if row[3] == paddle+1:
                                    #print(f"Module {localmodule} Bar {bar} Pixel {paddle}")
                                    ypos = 999.0
                                    continue

                    # print ypos, with no newline
                    print(f"{ypos:.3f} ",end='')

                print()

print()
print("earm.cdet.zpos = ")
for layer in range(NumLayers):
    for side in range(NumSides):
        for module in range(NumModules):
            for bar in range(NumBars):
                for paddle in range(NumPaddles):
                    if (layer == 0):
                        zpos = zpos1
                    else:
                        zpos = zpos2

                    # Search for the rows that match the current module, and PMT number
                    module_rows = data[np.where(data[:,0] == module+1)]
                    for row in module_rows:
                        if row[1] == side+1:
                            if row[2] == bar+1:
                                if row[3] == paddle+1:
                                    #print(f"Module {module} Bar {bar} Pixel {paddle}")
                                    zpos = 999.0
                                    continue

                    # print zpos, with no newline
                    print(f"{zpos:.3f} ",end='')
                print()