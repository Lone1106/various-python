import pygame, sys, random
##########

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()

        self.uncharged = pygame.image.load(path)
        self.charged = pygame.image.load("assets/spaceship_charged.png")

        self.image = self.uncharged
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.shield_surface = pygame.image.load("assets/shield.png")
        self.health = 5
 
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constraint()

        self.display_health()

    def screen_constraint(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280

        if self.rect.left <= 0:
            self.rect.left = 0

    def display_health(self):
        for index, shield in enumerate(range(self.health)):
            screen.blit(self.shield_surface, (10 + index * 40, 10))

    def get_damage(self, damage_amount):
        self.health -= damage_amount

    def charge(self):
        self.image = self.charged

    def discharge(self):
        self.image = self.uncharged

class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        if self.rect.centery >= 760:
            self.kill()

class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed

        if self.rect.centery <= -50:
            self.kill()

##########

def main_game():
    global laser_active

    laser_group.draw(screen)
    laser_group.update()

    spaceship_group.draw(screen)
    spaceship_group.update()
    meteors_group.draw(screen)
    meteors_group.update()


    #Collision
    if pygame.sprite.spritecollide(spaceship_group.sprite, meteors_group, True):
        spaceship.get_damage(1)

    
    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteors_group, True)

    #Laser Timer
    if pygame.time.get_ticks() - laser_timer >= 1000:
        laser_active = True
        spaceship_group.sprite.charge()

    return 1

def game_over():
    text_surfrace = game_font.render("Game Over", True, (255,255,255))
    text_rect = text_surfrace.get_rect(center = (640, 330))
    screen.blit(text_surfrace, text_rect)

    score_surfrace = game_font.render(f"Score: {score}", True, (255,255,255))
    score_rect = score_surfrace.get_rect(center = (640, 390))
    screen.blit(score_surfrace, score_rect)

##########

pygame.init()

pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

game_font = pygame.font.Font("assets/LazenbyCompSmooth.ttf", 60)

score = 0
laser_timer = 0
laser_active = False

#Groups
spaceship = SpaceShip("assets/spaceship.png", 640, 500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor = Meteor("assets/Meteor1.png", 640, 50, 1, 5)
meteors_group = pygame.sprite.Group()
meteors_group.add(meteor)

laser_group = pygame.sprite.Group()

#Create Userevent and Timer
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 200)

##########

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == METEOR_EVENT:
            meteor_path = random.choice(["assets/Meteor1.png", "assets/Meteor2.png", "assets/Meteor3.png"])
            random_x = random.randint(40, 1240)
            random_y = random.randint(-500, -50)
            random_x_speed = random.randint(-1, 1)
            random_y_speed = random.randint(1, 6)
            meteor = Meteor(meteor_path, random_x, random_y, random_x_speed, random_y_speed)
            meteors_group.add(meteor)

        if event.type == pygame.MOUSEBUTTONDOWN and laser_active:
            laser = Laser("assets/Laser.png", event.pos, 10)
            laser_group.add(laser)
            laser_active = False
            laser_timer = pygame.time.get_ticks()
            spaceship_group.sprite.discharge()

        if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
            spaceship_group.sprite.health = 5
            meteors_group.empty()
            score = 0


    screen.fill((42,45,51))
    

    if spaceship_group.sprite.health > 0:
        score += main_game()

    else:
        game_over()


    pygame.display.update()

    clock.tick(60)