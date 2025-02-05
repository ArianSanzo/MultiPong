import math


def normalize_angle(angle):
    """Normalizes an angle between -pi and pi"""
    if angle == math.pi:
        new_angle = angle
    else:
        new_angle = ((angle + math.pi) % (2 * math.pi)) - math.pi
    return new_angle
