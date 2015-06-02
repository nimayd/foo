#!/usr/bin/env python

import sys

def foo(*args):

# prints a rectangle to stdout with dimensions of width and height at a square offset

    if (len(sys.argv) > 3):
    	width = int(sys.argv[1]) - 2 # width/height minus corners
    	height = int(sys.argv[2]) - 2
    	offset = int(sys.argv[3]) * " "
        
	if (width <= -2 or height <= -2):	# widths/heights <= 0 do not form a rectangle
	    return

	else:
	    top = offset + "+"
            side = offset + "|"
	    if (width > -1):
	        side += " " * width + "|"
		top +=  "-" * width + "+"

            for i in range(0,len(offset)):	# sets up height offset
	        print
            print(top)
            for i in range(0, height):
	        print(side)
	    if (height > -1):
            	print(top)

    else:
        print("Enter arguments in order: width height offset")

foo(sys.argv)
