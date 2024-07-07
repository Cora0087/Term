"""
    求矩形相交的面积
    box   = [gx1, gy1, gx2, gy2]
    boxes = [cx1, cy1, cx2, cy2]

    box   = np.array([2, 2, 20, 25])
    boxes = np.array([15, 12, 25, 21])
"""
import numpy as np


def calculate_area(box, boxes):
    gx1, gy1, gx2, gy2 = box
    cx1, cy1, cx2, cy2 = boxes

    ix1 = max(gx1, cx1)
    iy1 = max(gy1, cy1)
    ix2 = min(gx2, cx2)
    iy2 = min(gy2, cy2)

    if ix1 < ix2 and iy1 < iy2:

        width = ix2 - ix1
        height = iy2 - iy1
        area = width * height
        return area
    else:
        # No intersection
        return 0


box = np.array([2, 2, 20, 25])
boxes = np.array([15, 12, 25, 21])
area = calculate_area(box, boxes)
print("矩形相交的面积:", area)