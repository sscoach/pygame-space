class BaseScene:

    def on_begin(self, **kwargs):
        pass

    def on_end(self):
        pass

    def on_key_down(self, key):
        pass

    def on_key_up(self, key):
        pass

    def on_update(self, delta_seconds):
        pass

    def on_render(self, surface):
        pass
    