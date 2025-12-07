import pygame
from projectile import Projectile

class Tower:
    def __init__(self, x, y, tower_type="basic"):
        self.x = x
        self.y = y
        self.range = 150
        self.cooldown = 60
        self.timer = 0
        self.type = tower_type
        self.projectiles = []

        if self.type=="fast": self.cooldown=20
        elif self.type=="slow": self.cooldown=100
        elif self.type=="long": self.range=250

    def update(self, enemies):
        self.timer +=1
        if self.timer >= self.cooldown:
            target = self.find_target(enemies)
            if target:
                self.projectiles.append(Projectile(self.x, self.y, target))
                self.timer = 0
        for proj in self.projectiles[:]:
            proj.move()
            if not proj.active:
                self.projectiles.remove(proj)

    def find_target(self, enemies):
        for enemy in enemies:
            dx = enemy.x - self.x
            dy = enemy.y - self.y
            if (dx**2 + dy**2)**0.5 <= self.range:
                return enemy
        return None

    def draw(self, screen):
        color = (0,255,0) if self.type=="basic" else (0,0,255) if self.type=="fast" else (255,0,255)
        pygame.draw.rect(screen, color, (self.x-15,self.y-15,30,30))
        pygame.draw.circle(screen, color, (self.x,self.y), self.range,1)
        for proj in self.projectiles:
            proj.draw(screen)
