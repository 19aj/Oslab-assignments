import random
import time
import math
import threading
import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

class Starship(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width = 48
        self.height = 48
        self.center_x = SCREEN_WIDTH // 2
        self.center_y = 32
        self.angle = 0
        self.score = 0
        self.healt = 3
        self.speed = 4
        self.bullet_list = []
        self.fire_sound = arcade.load_sound(":resources:sounds/laser4.wav")
        self.healt_image = arcade.load_texture("as12.Infinity War/Health.jpg")
        
    def fire(self):
        self.bullet_list.append(Bullet(self))
        arcade.play_sound(self.fire_sound)

class Enemy(arcade.Sprite):
    def __init__(self):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png ")
        self.center_x = random.randint(0+24, SCREEN_WIDTH-24)
        self.center_y = SCREEN_HEIGHT + 24
        self.width = 48
        self.height = 48
        self.speed = 4
        self.bullet_list = []

    def move(self):
        self.center_y -= self.speed

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x 
        self.center_y = host.center_y
        self.speed = 10
        self.angle = host.angle 

    def move(self):
        a = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(a)
        self.center_y += self.speed * math.cos(a)

class Explosion(arcade.Sprite):
    def __init__(self, x, y, beg ):
        super().__init__("as12.Infinity War/Explosion.jpg")
        self.width = 50
        self.height = 50
        self.center_x = x
        self.center_y = y
        self.show_time = 0.5
        self.start_time = beg

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Fall of Reach")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background_image = arcade.load_texture("as12.Infinity War/Background.jpg")
        self.gameover_image = arcade.load_texture("as12.Infinity War\Game Over.jpg")
        self.gameover_sound = arcade.load_sound(":resources:sounds/gameover3.wav")
        self.me = Starship()
        self.enemy_list = []
        self.check_lose = False
        self.destroy_sound = arcade.load_sound(":resources:sounds/gameover4.wav")
        self.explosion_list = []
        self.my_thread = threading.Thread(target=self.add_enemy)
        self.my_thread.start()

    def add_enemy(self):
        while True:
            self.enemy_list.append(Enemy())
            for enemy in self.enemy_list:
                enemy.speed *= 1.04
            time.sleep(random.randint(1, 6))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)
        self.me.draw()
        for enemy in self.enemy_list:
            enemy.draw()
        for bullet in self.me.bullet_list:
            bullet.draw()
        arcade.draw_text(f"Score: {self.me.score}", 500, 15, arcade.color.GREEN_YELLOW, 16)
        for i in range(self.me.healt):
            arcade.draw_lrwh_rectangle_textured(32 * i, 5, 32, 32, self.me.healt_image)
        for explosion in self.explosion_list:
            explosion.draw()
        if self.check_lose == True:
            arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.gameover_image)

    def on_update(self, delta_time: float):

        for enemy in self.enemy_list:
            enemy.move()
            if enemy.center_y < 0:
                self.enemy_list.pop(self.enemy_list.index(enemy))
                self.me.healt -= 1
                arcade.play_sound(self.gameover_sound)

        if self.me.healt <= 0:
            self.check_lose = True
            return

        for bullet in self.me.bullet_list:
            bullet.move()
            if bullet.center_y > 700 or bullet.center_y < 0 or bullet.center_x > 600 or bullet.center_x < 0:
                self.me.bullet_list.pop(self.me.bullet_list.index(bullet))

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    arcade.play_sound(self.destroy_sound)
                    self.explosion_list.append(Explosion(enemy.center_x, enemy.center_y, time.time()))
                    self.me.bullet_list.pop(self.me.bullet_list.index(bullet))
                    self.enemy_list.pop(self.enemy_list.index(enemy))
                    self.me.score += 1

        for explosion in self.explosion_list:
            if time.time() - explosion.start_time > explosion.show_time:
                self.explosion_list.pop(self.explosion_list.index(explosion))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE:
            self.me.fire()
        if symbol == arcade.key.LEFT:
            self.me.angle += 15
        if symbol == arcade.key.RIGHT:
            self.me.angle -= 15

def main() :
    my_game = Game()
    arcade.run()

if __name__ == "__main__":
    main()