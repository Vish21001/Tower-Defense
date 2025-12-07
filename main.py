import pygame, sys, json
from tower import Tower
from enemy import Enemy
from map import Map
from powerup import PowerUp

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

map_grid = Map()
towers = []
enemies = []
powerups = []
enemy_spawn_timer = 0
level = 1
lives = 10
money = 100
score = 0

# Load leaderboard
try:
    with open("leaderboard.json","r") as f:
        leaderboard=json.load(f)
except:
    leaderboard=[]

running=True
while running:
    screen.fill((50,50,50))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            if money>=50 and map_grid.is_valid_tile(x,y):
                towers.append(Tower(x,y,"basic"))
                money-=50

    enemy_spawn_timer +=1
    if enemy_spawn_timer>120:
        enemies.append(Enemy(path=map_grid.path))
        enemy_spawn_timer=0

    for enemy in enemies[:]:
        enemy.move()
        if enemy.reached_end():
            lives -=1
            enemies.remove(enemy)
        elif enemy.health <=0:
            enemies.remove(enemy)
            score +=10
            money +=20
            # Chance spawn powerup
            import random
            if random.randint(0,4)==0:
                powerups.append(PowerUp(enemy.x, enemy.y))

    for tower in towers:
        tower.update(enemies)

    # Update powerups
    for p in powerups[:]:
        p.fall()
        if pygame.Rect(tower.x-15,tower.y-15,30,30).colliderect(p.get_rect()):
            p.active=False
            if p.type=="extraLife": lives+=1
            elif p.type=="moneyBoost": money+=50
            elif p.type=="towerBoost":
                for t in towers: t.range+=50
    powerups = [p for p in powerups if p.active]

    map_grid.draw(screen)
    for tower in towers: tower.draw(screen)
    for enemy in enemies: enemy.draw(screen)
    for p in powerups: p.draw(screen)

    font=pygame.font.SysFont(None,30)
    hud=font.render(f"Lives:{lives}  Money:{money}  Score:{score}  Level:{level}",True,(255,255,255))
    screen.blit(hud,(10,10))

    pygame.display.flip()
    clock.tick(60)

    if lives<=0:
        print("Game Over! Score:",score)
        leaderboard.append(score)
        with open("leaderboard.json","w") as f:
            json.dump(leaderboard,f)
        running=False

pygame.quit()
sys.exit()
