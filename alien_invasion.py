import sys
import pygame
from settings import Settings

class AlienInvasion:
    '''
        Class to manage the game assets and the behaviour
    '''

    def __init__(self):
        '''
            Initializing the game, and creating the game resources
        '''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')


    def run_game(self):
        '''
            Starting the main loop for the game
        '''
        while True:
            # Watching for keypress events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during eadh pass of the loop
            self.screen.fill(self.settings.bg_colour)

            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()