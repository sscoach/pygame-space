from objects.object import Object


class Explosion(Object):
    def __init__(self, rect):
        super().__init__("assets/images/explosion.png")
        self.x = rect.center[0] - self.rect.center[0]
        self.y = rect.center[1] - self.rect.center[1]
        self.duration = 0.3

    def update(self, delta_seconds):
        super().update(delta_seconds)
        self.duration -= delta_seconds

    def is_finished(self):
        return self.duration <= 0
