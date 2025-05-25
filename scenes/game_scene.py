import pygame

from objects.alien import Alien
from objects.ufo import Ufo
from objects.fighter import Fighter
from objects.beam import Beam
from objects.bunker import Bunker
from objects.explosion import Explosion

from constants import *
from scenes.base_scene import BaseScene

from scene_manager import SceneManager


class GameScene(BaseScene):
    def __init__(self):
        self.fighter = None
        self.beams = []
        self.bunkers = []
        self.aliens = []
        self.ufos = []
        self.bombs = []
        self.explosions = []

        self.shoot_sound = pygame.mixer.Sound("assets/sounds/shoot.wav")
        self.invaderkilled_sound = pygame.mixer.Sound("assets/sounds/invaderkilled.wav")
        self.ufo_appear_sound = pygame.mixer.Sound("assets/sounds/ufo_lowpitch.wav")
        self.ufo_killed_sound = pygame.mixer.Sound("assets/sounds/ufo_highpitch.wav")
        self.explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")
        self.shoot_sound.set_volume(0.05)
        self.invaderkilled_sound.set_volume(0.05)
        self.ufo_appear_sound.set_volume(0.05)
        self.ufo_killed_sound.set_volume(0.05)
        self.explosion_sound.set_volume(0.05)

        self.score_font = pygame.font.Font(None, 30)
        self.score = 0

        self.ufo_timer = 0


    def on_begin(self, **kwargs):
        self.fighter = Fighter()
        self.score = 0
        for y in range(2):  # y: 0, 1
            for x in range(3):  # x: 0, 1, 2
                alien = Alien()
                self.aliens.append(alien)
                alien.x = 70 + 50 * x
                alien.y = 100 + 70 * y

        for x in range(3):
            bunker = Bunker(50 + x * 160, SCREEN_HEIGHT - 80)
            self.bunkers.append(bunker)

    def on_end(self):
        self.fighter = None
        self.beams.clear()
        self.bunkers.clear()
        self.aliens.clear()
        self.ufos.clear()
        self.bombs.clear()
        self.explosions.clear()

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
                self.score -= 1
                print('score', self.score)
            else:
                target = beam.check_collision(self.aliens + self.ufos)
                if target:
                    self.explosions.append(Explosion(target.rect))
                    self.beams.remove(beam)

                    if target in self.aliens:
                        self.aliens.remove(target)
                        self.invaderkilled_sound.play()

                        self.score += 50
                    else:
                        self.ufos.remove(target)
                        self.ufo_killed_sound.play()

                        self.score += 1000

                    if len(self.aliens) == 0:
                        print("Game Clear")
                        SceneManager.instance.change("game_over", score=self.score)

        for bunker in self.bunkers:
            bunker.update(delta_seconds)
            target = bunker.check_collision(self.bombs + self.beams)
            if target:
                if target in self.bombs:
                    self.bombs.remove(target)
                elif target in self.beams:
                    self.beams.remove(target)

                bunker.hp -= 1
                bunker.make_red()
                if bunker.hp <= 0:
                    self.bunkers.remove(bunker)


        for alien in self.aliens:
            alien.update(delta_seconds)

            bomb = alien.shoot()
            if bomb:
                self.bombs.append(bomb)

            if alien.check_collision([self.fighter]):
                self.explosions.append(Explosion(self.fighter.rect))
                self.explosions.append(Explosion(alien.rect))
                self.aliens.remove(alien)
                self.explosion_sound.play()
                print("Game Over")
                SceneManager.instance.change("game_over", score=self.score)
                break

        for ufo in self.ufos:
            ufo.update(delta_seconds)

        self.ufo_timer += delta_seconds
        if 10 < self.ufo_timer:
            self.ufo_timer = 0
            ufo = Ufo()
            ufo.x = 0
            ufo.y = 100
            self.ufos.append(ufo)
            self.ufo_appear_sound.play()

        for bomb in self.bombs:
            bomb.update(delta_seconds)
            if SCREEN_HEIGHT < bomb.y:
                self.bombs.remove(bomb)
            else:
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

        if Alien.should_change_direction:
            Alien.should_change_direction = False

            for alien in self.aliens:
                alien.direction_x *= -1
                alien.move(0, 50)


    def on_render(self, surface):
        self.fighter.draw(surface)
        for beam in self.beams:
            beam.draw(surface)

        for bunker in self.bunkers:
            bunker.draw(surface)

        for alien in self.aliens:
            alien.draw(surface)

        for ufo in self.ufos:
            ufo.draw(surface)

        for bomb in self.bombs:
            bomb.draw(surface)

        for explosion in self.explosions:
            explosion.draw(surface)

        text = self.score_font.render(f"Score: {self.score}", True, (255, 255, 0))
        text_rect = text.get_rect(center=(surface.get_width() / 2, 15))
        surface.blit(text, text_rect)