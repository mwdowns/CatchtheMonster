import pygame, random, time, math

KEY_W = 119
KEY_S = 115
KEY_A = 97
KEY_D = 100
ENTER = 13

class Monster(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.change_dir = 1
        self.direction = 1

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > 512:
            self.x = 0
        if self.x < 0:
            self.x = 512
        if self.y < 0:
            self.y = 480
        if self.y > 480:
            self.y = 0

        self.monsterMove()

    def monsterMove(self):
        self.change_dir -= 1

        if self.change_dir <= 0:
            self.change_dir = 120
            self.direction = random.randint(0, 3)
            if self.direction == 0:
                self.speed_x = 0
                self.speed_y = 5
            elif self.direction == 1:
                self.speed_x = 5
                self.speed_y = 0
            elif self.direction == 2:
                self.speed_x = 0
                self.speed_y = -5
            else:
                self.speed_x = -5
                self.speed_y = 0


class Hero(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def heroMove(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_W:
                print "%d, %d" % (self.x, self.y)
                # self.speed_x = 0
                self.speed_y = -4
            elif event.key == KEY_S:
                print "%d, %d" % (self.x, self.y)
                # self.speed_x = 0
                self.speed_y = 4
            elif event.key == KEY_A:
                print "%d, %d" % (self.x, self.y)
                self.speed_x = -4
                # self.speed_y = 0
            elif event.key == KEY_D:
                print "%d, %d" % (self.x, self.y)
                self.speed_x = 4
                # self.speed_y = 0

        if event.type == pygame.KEYUP:
            if event.key == KEY_W:
                print "%d, %d" % (self.x, self.y)
                # self.speed_x = 0
                self.speed_y = 0
            elif event.key == KEY_S:
                print "%d, %d" % (self.x, self.y)
                # self.speed_x = 0
                self.speed_y = 0
            elif event.key == KEY_A:
                print "%d, %d" % (self.x, self.y)
                self.speed_x = 0
                # self.speed_y = 0
            elif event.key == KEY_D:
                print "%d, %d" % (self.x, self.y)
                self.speed_x = 0
                # self.speed_y = 0

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > 450:
            self.x = 450
        elif self.x < 30:
            self.x = 30
        elif self.y < 30:
            self.y = 30
        elif self.y > 415:
            self.y = 415

    def collides(self, monster):
        if math.sqrt(((self.x - monster.x)** 2) + ((self.y - monster.y) ** 2)) < 32:
            print "You hit the monster"
            return True


def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)
    red_color = (255, 0, 0)

    # initialize the pygame framework
    pygame.init()
    pygame.mixer.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    #sounds
    lose_sound = pygame.mixer.Sound("sounds/lose.wav")
    win_sound = pygame.mixer.Sound("sounds/win.wav")
    background_music = pygame.mixer.Sound("sounds/music.wav")

    #fonts
    font = pygame.font.Font(None, 40)


    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background_image = pygame.image.load("images/background.png").convert_alpha()
    hero_image = pygame.image.load("images/hero.png").convert_alpha()
    monster = Monster(100, 10)
    hero = Hero(250, 240)
    # game loop
    stop_game = False
    dead = False
    while not stop_game:
        # look through user events fired

        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            hero.heroMove(event)

            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        monster.update()
        hero.update()
        # fill background color
        screen.fill(blue_color)
        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (hero.x, hero.y))
        if hero.collides(monster):
            dead = True
            win_sound.play()
        if dead == True:
            text = font.render("YOU WIN!!", True, (255, 0, 0))
            screen.blit(text, (200, 200))
            text2 = font.render("Do you want to play again?", True, red_color)
            screen.blit(text2, (90, 250))
        else:
            monster_image = pygame.image.load("images/monster.png").convert_alpha()
            screen.blit(monster_image, (monster.x, monster.y))
        # update the canvas display with the currently drawn frame
        pygame.display.update()
        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
