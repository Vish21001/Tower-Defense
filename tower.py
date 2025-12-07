import pygame
import math

class Tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.range = 150
        self.cooldown = 60  # frames
        self.timer = 0

    def update(self, enemies):
        self.timer += 1
        if self.timer >= self.cooldown:
            target = self.find_target(enemies)
            if target:
                # Shoot logic here (projectile, damage)
                target.health -= 10
                self.timer = 0

    def find_target(self, enemies):
        for enemy in enemies:
            dist = math.hypot(enemy.x - self.x, enemy.y - self.y)
            if dist <= self.range:
                return enemy
        return None

    def draw(self, screen):
        pygame.draw.rect(screen, (0,255,0), (self.x-15, self.y-15, 30,30))
        # Optional: draw range circle
        pygame.draw.circle(screen, (0,255,0), (self.x, self.y), self.range, 1)
