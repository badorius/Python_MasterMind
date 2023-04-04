import pygame

pygame.init()

width = 800
height = 800
white_colour = (255, 255, 255)

game_window = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Our game loop is now within a function
def run_game_loop():
    while True:
        # Handle events
        events = pygame.event.get()
        # Loops for all occurring events
        for event in events:
            # Checks if any of them is the QUIT event
            if event.type == pygame.QUIT:
                # Breaks the game loop by exiting the whole function
                return
              
        # Execute logic
        # Update display
        game_window.fill(white_colour)
        pygame.display.update()
        
        clock.tick(60)
        
# Calls the run_game_loop function       
run_game_loop()
  
pygame.quit()
quit()