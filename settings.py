class Settings:
    '''
        A class to store all the settings for alien invasion 
    '''

    def __init__(self):
        '''Initialize the game settings'''
        #Screen Settings 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        #Ship settings 
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60 ,60)
        self.bullets_allowed = 3

        #Alien Settings 
        self.fleet_drop_speed = 10

        # Scoring
        self.alien_points = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Score increase per wave
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Game Settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = .3

        #Fleet direction of 1 === right , -1 === left
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase the speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.score_scale * self.alien_points)

    