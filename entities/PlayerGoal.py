from core.Arc import Arc


class PlayerGoal(Arc):
    def __init__(self, x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite, player,
                 color=(255, 255, 0)):
        super().__init__(x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite, color)
        self._player = player

    def get_player(self):
        return self._player

    def draw(self, screen):
        super().draw(screen)
