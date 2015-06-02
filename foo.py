#!/usr/bin/env python

import sys

'''
def main(*args):

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
'''
def main(*args):
    parsed = parse(sys.argv)
    if (parsed):
        lines = makelines(parsed)
        create(lines)

def parse(dims):
    if (len(dims) != 4):
        print("Enter three integer arguments in order: width height offset")
        return None

    for dim in dims[1:]:
        try:
            int(dim)
        except ValueError:
            print('Please enter only integer values.')
            return None
        if (dim <= 0):
            print('Dimensions must be >= 1.')
            return None
    
    return (int(dims[1]) - 2, int(dims[2]) - 2, int(dims[3]) * ' ')

def makelines(parsed_dims):
    width = parsed_dims[0]
    height = parsed_dims[1]
    offset = parsed_dims[2]
    
    top = offset + '+'
    side = offset + '|'
    if (width > -1):
        side += ' ' * width + '|'
        top += '-' * width + '+'

    return (width, height, len(offset), top, side)
    

def create(nums):
    width = nums[0]
    height = nums[1]
    offset = nums[2]
    top = nums[3]
    side = nums[4]

    for i in range (0, offset):
        print
    print(top)
    for j in range (0, height):
        print(side)
    if (height > -1):
        print(top)

main(sys.argv)
