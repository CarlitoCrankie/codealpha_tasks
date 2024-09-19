# jarvisGUI.py
import time
import pygame

class imageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile(self, filename, id=None):
        if id is None:
            id = filename
        self.pics[id] = pygame.image.load(filename).convert()

    def loadFromSurface(self, surface, id):
        self.pics[id] = surface.convert_alpha()

    def render(self, surface, id, clear=False):
        if clear:
            surface.fill((5, 2, 23))
        scaled_image = pygame.transform.smoothscale(self.pics[id], surface.get_size())
        surface.blit(scaled_image, (0, 0))

pygame.display.init()
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
handler = imageHandler()

def display():
    for i in range(23):
        handler.loadFromFile(rf"Data\exctracted-ezgif\frame_{i:02}_delay-0.09s.gif", str(i + 1))

display()

def face():
    frame_count = 23
    current_frame = 0
    global running  # Make `running` a global variable
    running = True  # Use this to control the Pygame loop

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handler.render(screen, str(current_frame + 1), True)
        pygame.display.flip()
        time.sleep(0.2)
        current_frame = (current_frame + 1) % frame_count

    pygame.quit()

def stop_face():
    global running
    running = False
