#! python
# This code is based off a video series provided by Sentdex from YouTube.  The
# game created is a "racing game", of sorts, in which the user tries to avoid
# obstacles.
import pygame


# Initiallize pygame and all its modules.  Must be done before anything else
# can be done with pygame.
pygame.init

# Setup a window - works sort of like TKinter.  The display.set_mode function
# takes in a tuple so it must be put inside (), otherwise the function would
# treat the two numbers as separate inputs.
# gameDisplay = pygame.display.set_mode((800, 600))

# Game size allowing for resizing of window and allowing for spacial reference
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Color definitions.  Pygame does not have default color references built in.
# Colors defined in RGB tuple
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

car_width = 86

pygame.display.set_caption('A Bit Racey')

# Set the game's clock
clock = pygame.time.Clock()

# Loading car asset
carImg = pygame.image.load('car_asset.png')


# Displaying car in window
def car(x, y):
    # blit is drawing to the surface
    gameDisplay.blit(carImg, (x, y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0

    # Setting a condition that will always break user from the game loop - user
    # crashes into object, game resets.
    gameExit = False

    # EVENT HANDLING LOOP
    # "Game loop" or "Main loop" is where all the game logic is put.
    while not gameExit:
        for event in pygame.event.get():
            # pygame.QUIT will be when someone closes the window
            if event.type == pygame.QUIT:
                # Break out of loop
                gameExit = True

            # Moving the car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            # Reset the x_change variable on key release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)
        car(x, y)

        # Crash logic
        if x > display_width - car_width or x < 0:
            gameExit = True

        # pygame.display.update allows you to put in a single parameter to be
        # updated, leaving it blank will update the whole "surface"/"window".
        # pygame.display.flip() will update the whole thing.
        pygame.display.update()

        # Define frames per second
        clock.tick(60)


game_loop()

# Exiting the game
pygame.quit()
quit
