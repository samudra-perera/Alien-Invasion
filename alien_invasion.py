import sys

import pygame

class AlienInvasion:
    '''
        Class to manage the game assets and the behaviour
    '''

    def __init__(self):
        '''
            Initializing the game, and creating the game resources
        '''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
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
            
            #Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()