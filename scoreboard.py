import pygame.font

class Scoreboad:
    """A Class to record all the soring information"""

    def __init__(self, ai_game):
        """Initialize scorekeep attributes"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font Settings for scoring
        self.text_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Prep the inital score
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_colour, self.settings.bg_colour)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displaying the score on the screens"""
        self.screen.blit(self.score_image, self.score_rect)