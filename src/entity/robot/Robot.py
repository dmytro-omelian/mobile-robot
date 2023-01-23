import pygame

from constant.constants import BLOCK_SIZE, WINDOW_SIZE
from entity.robot.Battery import Battery
from entity.robot.Trash import Trash


class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.trash = Trash()
        self.battery = Battery()

        self.img_can = pygame.image.load("src/resources/can.png")
        self.img_can = pygame.transform.scale(self.img_can, (3 * BLOCK_SIZE, 3 * BLOCK_SIZE))

        self.img_robot = pygame.image.load("src/resources/robot.png")
        self.img_robot = pygame.transform.scale(self.img_robot, (3 * BLOCK_SIZE, 3 * BLOCK_SIZE))

        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def collect_can(self):
        self.trash.add()

    def can_collect_can(self):
        return self.trash.is_not_full()

    def clean_cans(self):
        self.trash.clean()

    def is_trash_empty(self):
        return self.trash.is_empty()

    def update(self, display):
        self.basic_trash(display)
        self.basic_battery(display)

    def dying_damage(self, amount):
        self.battery.damage(amount)

    def get_battery(self, amount):
        self.battery.charge(amount)

    def basic_battery(self, display):
        pygame.draw.rect(display, self.get_battery_color(self.battery.get_current()),
                         (10, 25, self.battery.get_current() / self.battery.get_ratio(), 25))
        pygame.draw.rect(display, (255, 255, 255), (10, 25, self.battery.get_bar_len(), 25), 4)

    def basic_trash(self, display):
        display.blit(self.img_can, (WINDOW_SIZE // 2 - 100, 10))

        text = self.font.render(f': {self.trash.get_current_size()} / {self.trash.get_max_size()}', True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_SIZE // 2, 40)
        display.blit(text, text_rect)

    def get_battery_color(self, battery):
        if battery < self.battery.get_max() // 3:
            return 255, 0, 0
        if battery > self.battery.get_max() // 3 * 2:
            return 127, 255, 0
        return 255, 255, 0

    def main(self, display):
        display.blit(self.img_robot, ((self.x - 1) * BLOCK_SIZE, (self.y - 1) * BLOCK_SIZE))

    def can_move(self):
        return self.battery.can_move()
