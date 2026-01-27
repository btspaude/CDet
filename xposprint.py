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

# Geometry parameters
length_paddle = 0.51 # 51 cm length
bar_thickness = 0.073 # 14 bars => 73 mm
mirror_thickness = 0.007 # 5mm mirros + 1mm gap on either side
yoffset = 0.075 # horizontal offset of subgroups relative to module center
zpos_ecal = 6.00
layer1_offset = 0.25
layer2_offset = 0.15


####################################### Nothing below here should change ###############
NumPaddlesPerSide = NumBars*(NumPaddles-2)*NumModules
xthickness = bar_thickness/NumBars;
xoffset = -1.0*xthickness*NumPaddlesPerSide/2.0

yleft = length_paddle/2.0 + mirror_thickness/2.0 
yright = -yleft

zpos1 = zpos_ecal - layer1_offset
zpos2 = zpos_ecal - layer2_offset

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
                        if row[1] == 2-side:
                            if row[2] == 14-bar:
                                if side==0:
                                    if row[3] == paddle+1:
                                        #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                        xpos = -999.0
                                        missingcounter = missingcounter + 1
                                        flag = True
                                else:
                                    if (17-row[3]) == paddle+1:
                                        #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                        xpos = -999.0
                                        missingcounter = missingcounter + 1
                                        flag = True

                    if (not flag):
                        paddlenumber = (bar + NumBars*module)*NumPaddles + paddle
                        sectionoffset = (2*layer + side)*NumPaddlesPerSide
                        #if (xpos == 999.0):
                        #    print(f"***{paddlenumber + sectionoffset}***",end='')
                        xpos = xoffset + xthickness*paddlenumber - xthickness*missingcounter



                    # print xpos, with no newline
                    print(f"{-xpos:.3f} ",end='')

                print()

for refj in range(1):
    for ref in range(16):
        print("999.000 ",end='')
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
                        if row[1] == 2-side:
                            if row[2] == 14-bar:
                                if side==0:
                                    if row[3] == paddle+1:
                                        #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                        ypos = -999.0
                                        missingcounter = missingcounter + 1
                                        flag = True
                                else:
                                    if (17-row[3]) == paddle+1:
                                        #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                        ypos = -999.0
                                        missingcounter = missingcounter + 1
                                        flag = True

                    # print ypos, with no newline
                    print(f"{ypos:.3f} ",end='')

                print()
        
for refj in range(1):
    for ref in range(16):
        print("999.000 ",end='')
    print()

print()
print("earm.cdet.zpos = ")
for layer in range(NumLayers):
    for side in range(NumSides):
        missingcounter = 0
        for module in range(NumModules):
            localmodule = module + NumModules*layer
            for bar in range(NumBars):
                for paddle in range(NumPaddles):
                    if (layer == 0):
                        zpos = zpos1
                    else:
                        zpos = zpos2

                    # Search for the rows that match the current module, and PMT number
                    module_rows = data[np.where(data[:,0] == localmodule+1)]
                    flag = False
                    for row in module_rows:
                        if row[1] == 2-side:
                            if row[2] == 14-bar:
                                if side==0:
                                    if row[3] == paddle+1:
                                        #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                        zpos = -999.0
                                        missingcounter = missingcounter + 1
                                        flag = True
                                else:
                                    if (17-row[3]) == paddle+1:
                                        #print(f"Module {localmodule} Side {side} Bar {bar} Pixel {paddle}")
                                        zpos = -999.0
                                        missingcounter = missingcounter + 1
                                        flag = True

                    # print zpos, with no newline
                    print(f"{zpos:.3f} ",end='')
                print()
        
for refj in range(1):
    for ref in range(16):
        print("999.000 ",end='')
print()
