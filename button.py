import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """Initialize Button Attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Setting properties and dimension of the button
        self.width, self.height = 200, 50
        self.button_colour = (0, 255, 0)
        self.text_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the buttons rect object and and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message
        self._prep_msg(msg)

