import pygame, sys, random
##########

pygame.init()

#Create screen
screen = pygame.display.set_mode((1280, 720))

#Create clock for Frame Rate
clock = pygame.time.Clock()

#Hide Mouse curser
pygame.mouse.set_visible(False)

#Import Images
wood_bg = pygame.image.load("assets/Wood_BG.png")
land_bg = pygame.image.load("assets/Land_BG.png")
water_bg = pygame.image.load("assets/Water_BG.png")
cloud_1 = pygame.image.load("assets/Cloud1.png")
cloud_2 = pygame.image.load("assets/Cloud2.png")
crosshair = pygame.image.load("assets/crosshair.png")
duck = pygame.image.load("assets/duck.png")

#Create Font
game_font = pygame.font.Font(None, 50)
text_surface = game_font.render("Game Over", True, (255,255,255))
text_rect = text_surface.get_rect(center = (640, 360))

#Variables
land_position_y = 560
land_speed = 1
water_positon_y = 640
water_speed = 1

crosshair_rect = crosshair.get_rect(center=(640, 360))

duck_list = []
#Create ducks
for _ in range(10):
    random_x = random.randint(70, 1200)
    random_y = random.randint(120, 600)
    duck_rect = duck.get_rect(center=(random_x, random_y))
    duck_list.append(duck_rect)

#Game Loop
while True:
    #Check for input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Place Mouse curser

        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center=event.pos)

        #Check mouseclick
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):           #crosshair_rect.colliderect(duck_rect):
                    del duck_list[index]



    #Place Images on Screen
    screen.blit(wood_bg, (0, 0))

    #Move images
    land_position_y += land_speed
    if land_position_y <= 520 or land_position_y >= 600:
        land_speed *= -1

    screen.blit(land_bg, (0, land_position_y))


    water_positon_y += water_speed
    if water_positon_y <= 600 or water_positon_y >= 700:
        water_speed *= -1

    #Place ducks
    for duck_rect in duck_list:
        screen.blit(duck, duck_rect)

    #Check winner
    if len(duck_list) == 0:
        screen.blit(text_surface, text_rect)


    screen.blit(water_bg,(0, water_positon_y))

    screen.blit(crosshair, crosshair_rect)

    screen.blit(cloud_1, (60, 50))
    screen.blit(cloud_1, (1000, 70))
    screen.blit(cloud_2, (600, 40))
    screen.blit(cloud_2, (400, 100))


    #Update screen
    pygame.display.update()

    #Limit Frames
    clock.tick(60)





