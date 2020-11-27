import pygame


# Simple graphing module. It pretty much just renders straight lines relative to
# the origin which, in this case, is the center of the window. 
#   After initing a window:
    #* Call clear() to erase the buffer
    #* Call drawing functions
    #* call update() to flip the buffer to screen
class Grapher:
    def __init__(self):
        self.__res_x = 800
        self.__res_y = 800
        self.__org_x = 400
        self.__org_y = 400
        self.__pixel_col = (255, 255, 255, 255)
        self.__clear_col = (0, 0, 0, 255)
        self.__font_size = 16
        self.__font_v_spacing = 15
        self.__font_line = 0
        
        # init window
        try:
            self.__window = pygame.display.set_mode((self.__res_x, self.__res_y))
            print("Grapher Initialized")
        except Exception as error:
            print("Failed to init grapher!")
            exit(1)
            
        # init fonts
        try:
            pygame.font.init()
            self.font = pygame.font.SysFont("freemono", 16)
            print("Fonts Initialized")
        except Exception as error:
            print("Failed to init fonts!")
            exit(1)
            
    # clear buffer
    def clear(self):
        self.__window.fill(self.__clear_col)
        self.__font_line = 0
    
    # display buffer
    def update(self):
        pygame.display.update()
        
    # draw line between two points relative to origin
    def draw_line(self, start_x, start_y, end_x, end_y):
        """Draw line between two points relative to origin"""
        sx = self.__org_x + start_x
        sy = self.__org_y + (start_y * -1)
        ex = self.__org_x + end_x
        ey = self.__org_y+ (end_y * -1)
        pygame.draw.line(self.__window, self.__pixel_col, (sx, sy), (ex, ey))
        
    # draw text at given coordinates
    def draw_text(self, text, pos_x, pos_y):
        """Draw 'text' (string) at pos_x, pos_y (int)"""
        surface = self.font.render(text, True, (255, 255, 255))
        self.__window.blit(surface, (pos_x, pos_y))
        
    # simulate a console-like output function
    def console_out(self, text):
        surface = self.font.render(text, True, (255, 255, 255))
        self.__window.blit(surface, (0, self.__font_v_spacing * self.__font_line))
        self.__font_line += 1
