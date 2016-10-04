import pygame
import random

class Ball(object):
    def __init__(self):
        self.x = random.randrange(10, 400)
        self.y = random.randrange(10, 400)
        self.speed_x = random.randrange(-10, 10)
        self.speed_y = random.randrange(-10, 10)
        self.radius = random.randrange(10, 40)
        self.color = (random.randrange(10, 255), random.randrange(10, 255), random.randrange(10, 255))

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if (self.x + self.radius) > width:
            self.speed_x = random.randrange(-10, -1)
        if (self.y + self.radius) > height:
            self.speed_y = random.randrange(-10, -1)
        if (self.x - self.radius) < 0:
            self.speed_x = random.randrange(1, 10)
        if (self.y - self.radius) < 0:
            self.speed_y = random.randrange(1, 10)

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################

    ball_list = [Ball(), Ball(), Ball(), Ball()]

    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        for ball in ball_list:
            ball.update(width, height)

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in ball_list:
            ball.render(screen)
        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
