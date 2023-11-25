import pygame

class Ship:
    '''
        A class to manage the ship
    '''

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #Load the ship image and get its rect
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store the decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''Update Ship Position based on movement flag'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #update rectangle property from self.x
        self.rect.x = self.x