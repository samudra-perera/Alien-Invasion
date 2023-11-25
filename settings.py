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
        self.ship_speed = 1.5