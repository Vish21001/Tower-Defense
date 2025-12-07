import pygame
import math

class Projectile:
    def __init__(self, x, y, target):
        self.x = x
        self.y = y
        self.target = target
        self.speed = 5
        self.damage = 10
        self.active = True

    def move(self):
        if not self.active or self.target is None:
            return
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            self.x += self.speed * dx/dist
            self.y += self.speed * dy/dist
        if dist < 5:
            self.target.health -= self.damage
            self.active = False

    def draw(self, screen):
        if self.active:
            pygame.draw.circle(screen, (255,255,0), (int(self.x), int(self.y)), 5)
