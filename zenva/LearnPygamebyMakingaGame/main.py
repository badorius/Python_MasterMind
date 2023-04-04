import pygame

pygame.init()

width = 800
height = 800
white_colour = (255, 255, 255)

# Creates the game window
game_window = pygame.display.set_mode((width, height))

# Creating a clock variable
clock = pygame.time.Clock()

# Game loop
while True:
    # What's inside this loop will be repeated continuosly
    
    # Handle events
    # Execute logic
    # Update display
    
    # Colors the background white
    game_window.fill(white_colour)
    # Updates the changes to the window 
    pygame.display.update()
    
    # Setting how many times per second we want to update the game window
    clock.tick(60)
  
pygame.quit()
quit()