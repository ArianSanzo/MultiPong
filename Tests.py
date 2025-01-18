import math

speed_x = 10 * math.cos(-math.pi/3)
speed_y = - 10 * math.sin(-math.pi/3)

print(speed_x, speed_y)

obj_and_ball_angle = math.atan2(-(50), -100) - math.pi
obj_and_ball_angle = ((obj_and_ball_angle + math.pi) % (2 * math.pi)) - math.pi

print(-math.pi/2)

print(obj_and_ball_angle)
