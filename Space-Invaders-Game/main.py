##########Imports
from turtle import Screen
import time
from player import Player
from enemies import Enemies
from scoreboard import Scoreboard

##########Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.tracer(0)

##########Variables

SHOT_SPEED = -20
game_on = True
player = Player((0, -250), 90)
enemies = Enemies()
scoreboard = Scoreboard()

##########Key Input

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(player.create_shot, "Up")

##########Game Loop

while game_on:
    time.sleep(0.1)
    screen.update()
    enemies.move()
    enemies.shoot()

    #Move shots
    #Player
    for shot in player.all_shots:
        shot.back(SHOT_SPEED)

    #Enemies
    for shot in enemies.all_shots:
        shot.back(-SHOT_SPEED)


    #Player Collision
    if player.xcor() > 280:
        player.stop_moving(280)

    elif player.xcor() < -280:
        player.stop_moving(-280)


    for shot in enemies.all_shots:
        if player.distance(shot) < 15:
            game_on = False
            scoreboard.game_over()


    #Enemy Collision
    for enemy in enemies.all_enemies:
        if enemy.xcor() > 280:
            enemies.bounce_right()
        
        elif enemy.xcor() < -280:
            enemies.bounce_right()


    
    #Collision with Shot and add score
    for shot in player.all_shots:
        for enemy in enemies.all_enemies:
            if enemy.distance(shot) < 20:
                enemy.goto(500, 500)
                shot.goto(500, 500)

                scoreboard.add_point()

                player.all_shots.remove(shot)
                enemies.all_enemies.remove(enemy)


                #Check if player won
                if len(enemies.all_enemies) == 0:
                    game_on = False
                    scoreboard.game_won()



##########
screen.exitonclick()
