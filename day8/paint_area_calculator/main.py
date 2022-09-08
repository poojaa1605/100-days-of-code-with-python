# paint area calculator
import math


def paint_cal(height1, width1, cover):
    area = height1 * width1
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans")


height = int(input("Height of the wall :   "))
width = int(input("Width of the wall  :   "))

coverage = 5

paint_cal(height1=height, width1=width, cover=coverage)
