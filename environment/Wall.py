from core.Arc import Arc
"""
Static walls of the game:

    For more info look for Arc comments.
"""


class Wall(Arc):
    def __init__(self, x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite,
                 color=(255, 255, 255)):
        super().__init__(x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite, color)

    def x_center(self):
        return super().x_center()

    def y_center(self):
        return super().y_center()

    def radius(self):
        return super().radius()

    def starting_angle(self):
        return super().starting_angle()

    def ending_angle(self):
        return super().ending_angle()

    def draw(self, screen):
        super().draw(screen)
