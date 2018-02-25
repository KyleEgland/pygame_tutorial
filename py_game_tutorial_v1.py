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
gameDisplay = pygame.display.set_mode((800, 600))

pygame.display.set_caption('A Bit Racey')

# Set the game's clock
clock = pygame.time.Clock()

# Setting a condition that will always break user from the game loop - user
# crashes into object, game resets.
crashed = False

# "Game loop" or "Main loop" is where all the game logic is put.
while not crashed:
    for event in pygame.event.get():
        # pygame.QUIT will be when someone closes the window
        if event.type == pygame.QUIT:
            # Break out of loop
            crashed = True
        # Print out events to console
        print(event)

    # pygame.display.update allows you to put in a single parameter to be
    # updated, leaving it blank will update the whole "surface"/"window".
    # pygame.display.flip() will update the whole thing.
    pygame.display.update()

    # Define frames per second
    clock.tick(60)


# Exiting the game
pygame.quit()
quit
