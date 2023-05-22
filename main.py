import sys
import pygame

pygame.init()

def play():
    print("Game screen will be here")

def menu():
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Cannon Man")
    screen = pygame.display.set_mode((960, 639))
    BG = pygame.image.load("background1.png")
    logo = pygame.image.load('logo3.png')

    pygame.display.Info().current_h
    pygame.display.Info().current_w
    pygame.time.Clock()

    class Button:
        def __init__(self, x, y, image, scale):
            self.image = image
            self.scale = scale
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.clicked = False

        def draw(self, surface):
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            surface.blit(self.image, (self.rect.x, self.rect.y))
            return action


    start_img = pygame.image.load('play1.png').convert_alpha()
    exit_img = pygame.image.load('quit.png').convert_alpha()
    on = pygame.image.load('on.png').convert_alpha()
    pause = pygame.image.load('off.png').convert_alpha()

    start_button = Button(362, 285, start_img, 1.2)
    exit_button = Button(383, 370, exit_img, 1)
    on_button = Button(860, 5, on, 0.6)
    pause_button = Button(905, 5, pause, 0.6)

    sound_on = False
    run = True
    while run:
        screen.blit(BG, (0, 0))
        screen.blit(logo, (158, 120))

        if start_button.draw(screen):
            play()
        if exit_button.draw(screen):
            pygame.quit()
            sys.exit()
        if on_button.draw(screen):
            pygame.mixer.music.unpause()
        if pause_button.draw(screen):
            pygame.mixer.music.pause()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

menu()
