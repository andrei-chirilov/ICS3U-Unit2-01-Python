#!/usr/bin/env python

# Created by: Andrei Chirilov
# Created on september 16
# This program will calculate the area and the perimetre of a circle
# with a radius of 15mm

import math


def main():
    print("If a circle has a radius of 15mm:")
    print("")
    print("area is {}mm^2".format(math.pi*15**2))
    print("perimeter is {}mm".format(2*math.pi*15))


if __name__ == "__main__":
    main()
