import pygame
import random

class PowerUp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.active = True
        self.type = random.choice(["extraLife", "moneyBoost", "towerBoost"])

    def fall(self):
        self.y += 2

    def draw(self, screen):
        if not self.active:
            return
        color = (255,105,180) if self.type=="extraLife" else (0,255,255) if self.type=="moneyBoost" else (255,255,0)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
