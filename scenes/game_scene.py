import pygame

from objects.alien import Alien
from objects.bunker import Bunker
from objects.fighter import Fighter
from objects.beam import Beam
from objects.explosion import Explosion

from constants import *
from objects.ufo import Ufo
from scenes.base_scene import BaseScene

from scene_manager import SceneManager


class GameScene(BaseScene):
    def __init__(self):
        self.fighter = None
        self.beams = []
        self.aliens = []
        self.ufos = []
        self.ufo_timer = 0
        self.bombs = []
        self.explosions = []
        self.bunkers = []

        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot.wav")
        self.invaderkilled_sound = pygame.mixer.Sound("assets/sounds/invaderkilled.wav")
        self.explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")
        self.ufo_sound = pygame.mixer.Sound("assets/sounds/ufo_lowpitch.wav")
        self.ufo_killed_sound = pygame.mixer.Sound("assets/sounds/ufo_highpitch.wav")
        self.shoot_sound.set_volume(0.05)
        self.invaderkilled_sound.set_volume(0.05)
        self.explosion_sound.set_volume(0.05)
        self.ufo_sound.set_volume(0.05)
        self.ufo_killed_sound.set_volume(0.05)
        self.score = 0
        self.miss_fire_count = 0

        self.score_font = pygame.font.Font(None, 30)

    def on_begin(self, **kwargs):
        self.score = 0
        self.fighter = Fighter()
        self.ufo_timer = 0
        for y in range(2):  # y: 0, 1
            for x in range(3):  # x: 0, 1, 2
                alien = Alien()
                self.aliens.append(alien)
                alien.x = 70 + 50 * x
                alien.y = 100 + 70 * y

        for x in range(3):
            bunker = Bunker()
            bunker.x = 50 + SCREEN_WIDTH / 3 * x
            bunker.y = SCREEN_HEIGHT - bunker.rect.height * 2 - self.fighter.rect.height
            self.bunkers.append(bunker)

    def on_end(self):
        self.fighter = None
        self.beams.clear()
        self.aliens.clear()
        self.ufos.clear()
        self.bombs.clear()
        self.explosions.clear()
        self.bunkers.clear()

    def on_key_down(self, key):
        if key == pygame.K_LEFT:
            self.fighter.direction_x = -1
        if key == pygame.K_RIGHT:
            self.fighter.direction_x = +1
        if key == pygame.K_SPACE:
            if len(self.beams) < 2:
                beam = Beam(self.fighter.x + self.fighter.image.get_width() / 2, self.fighter.y)
                self.beams.append(beam)
                self.shoot_sound.play()

    def on_key_up(self, key):
        if key == pygame.K_LEFT:
            self.fighter.direction_x = 0
        if key == pygame.K_RIGHT:
            self.fighter.direction_x = 0

    def on_update(self, delta_seconds):
        self.fighter.update(delta_seconds)
        for beam in self.beams:
            beam.update(delta_seconds)
            if beam.y < 0:
                self.beams.remove(beam)
                self.miss_fire_count += 1
                self.score -= 1
            else:
                target = beam.check_collision(self.aliens + self.ufos)
                if target:
                    self.explosions.append(Explosion(target.rect))
                    if target in self.aliens:
                        self.aliens.remove(target)
                        self.invaderkilled_sound.play()
                    if target in self.ufos:
                        self.ufos.remove(target)
                        self.ufo_killed_sound.play()
                    self.beams.remove(beam)
                    self.add_score(target)

                    if len(self.aliens) == 0:
                        print("Game Clear")
                        SceneManager.instance.change("game_over", score=self.score)

                target = beam.check_collision(self.bunkers)
                if target:
                    self.beams.remove(beam)

        for target in self.aliens:
            target.update(delta_seconds)

            bomb = target.shoot()
            if bomb:
                self.bombs.append(bomb)

            if target.check_collision([self.fighter]):
                self.explosions.append(Explosion(self.fighter.rect))
                self.explosions.append(Explosion(target.rect))
                self.aliens.remove(target)
                self.explosion_sound.play()
                print("Game Over")
                SceneManager.instance.change("game_over", score=self.score)
                break

        self.ufo_timer += delta_seconds
        if self.ufo_timer > 10:
            self.ufo_timer = 0
            self.ufos.append(Ufo())
            self.ufo_sound.play()

        for ufo in self.ufos:
            ufo.update(delta_seconds)
            if SCREEN_WIDTH < ufo.x:
                self.ufos.remove(ufo)

        for bomb in self.bombs:
            bomb.update(delta_seconds)
            if SCREEN_HEIGHT < bomb.y:
                self.bombs.remove(bomb)
            else:
                bunker = bomb.check_collision(self.bunkers)
                if bunker:
                    self.bombs.remove(bomb)
                    continue

                if bomb.check_collision([self.fighter]):
                    self.explosions.append(Explosion(self.fighter.rect))
                    self.bombs.remove(bomb)
                    self.explosion_sound.play()
                    print("Game Over")
                    SceneManager.instance.change("game_over", score=self.score)
                    break


        for explosion in self.explosions:
            explosion.update(delta_seconds)
            if explosion.is_finished():
                self.explosions.remove(explosion)

        for bunker in self.bunkers:
            bunker.update(delta_seconds)

        if Alien.should_change_direction:
            Alien.should_change_direction = False

            for target in self.aliens:
                target.direction_x *= -1
                target.move(0, 50)

    def add_score(self, target):
        self.score += target.score
        if self.miss_fire_count == 0:
            self.score += target.bonus_score
        self.miss_fire_count = 0

    def on_render(self, surface):
        self.fighter.draw(surface)
        for beam in self.beams:
            beam.draw(surface)

        for alien in self.aliens:
            alien.draw(surface)

        for ufo in self.ufos:
            ufo.draw(surface)

        for bunker in self.bunkers:
            bunker.draw(surface)

        for bomb in self.bombs:
            bomb.draw(surface)

        for explosion in self.explosions:
            explosion.draw(surface)

        # render score
        text = self.score_font.render(f"Score: {self.score}", True, (255, 255, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, 20))
        surface.blit(text, text_rect)
