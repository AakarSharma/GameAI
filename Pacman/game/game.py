import pygame
from pygame.locals import *
from numpy import loadtxt
import time
from math import ceil, floor
import random

# Constants for the game
WIDTH, HEIGHT = (30, 30)
WALL_COLOR = pygame.Color(0, 0, 255, 255)  # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255)  # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255)  # YELLOW
DOWN = (0, 1)
RIGHT = (1, 0)
TOP = (0, -1)
LEFT = (-1, 0)

STATIC_DIR = './static/'


class ghostclass:
    # This class is made to organize the function of ghost in the game
    def __init__(self, x, y, z):
        self.row = x
        self.col = y
        self.move_direction = z

    def draw_ghost(self, screen, number_of_ghost):
        '''
        This function is used to draw pacman of the game screen


        '''
        pos = (self.row, self.col)
        pixels = pixels_from_points(pos)
        if(number_of_ghost == 1):
            screen.blit(pygame.transform.scale(ghostimage, (25, 25)), pixels)
        if(number_of_ghost == 2):
            screen.blit(pygame.transform.scale(ghostimage2, (25, 25)), pixels)
        if(number_of_ghost == 3):
            screen.blit(pygame.transform.scale(ghostimage3, (25, 25)), pixels)

    def ghostposition(self):
        '''
        This funtion is used to return the position of the ghost when needed
        '''
        return (self.row, self.col)

    def updateposition(self, new_position_tuple):
        '''
                This function is used to update the position of the ghost after all the computation done in the program
        '''
        self.row = new_position_tuple[0]
        self.col = new_position_tuple[1]
        return

    def find_move_direction(self):
        '''
        This function is used to return the moving direction of the ghost 
        '''
        return self.move_direction

    def update_move_direction(self, new_direction):
        '''
                This function is used to update the 
        '''

        self.move_direction = new_direction
        return

# Draws a rectangle for the wall


def draw_wall(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])

# Draws a rectangle for the player


def draw_pacman(screen, pos, direction_to_point):
    pixels = pixels_from_points(pos)

    if counter_to_maintain_pacman_animation % 4 == 0:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(
            myimage, (30, 30)), direction_to_point), pixels)
    if counter_to_maintain_pacman_animation % 4 == 1:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(
            myimage1, (30, 30)), direction_to_point), pixels)
    if counter_to_maintain_pacman_animation % 4 == 2:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(
            myimage2, (30, 30)), direction_to_point), pixels)
    if counter_to_maintain_pacman_animation % 4 == 3:
        screen.blit(pygame.transform.rotate(pygame.transform.scale(
            myimage3, (30, 30)), direction_to_point), pixels)


# Draws a rectangle for the coin
def draw_coin(screen, pos):
    pixels = pixels_from_points(pos)
    temp_list = [pixels[0], pixels[1]]
    temp_list[0] += WIDTH//2
    temp_list[1] += HEIGHT//2
    pixels = tuple(temp_list)

    pygame.draw.circle(screen, COIN_COLOR, pixels, 3)


# Uitlity functions
def add_to_pos(pos, pos2):

    return (pos[0]+pos2[0], pos[1]+pos2[1])


def pixels_from_points(pos):

    return (pos[0]*WIDTH, pos[1]*HEIGHT)


def for_displaying_time_elapsed():
    '''
    This function is used to calculate the time elapsed from the start
    '''
    current_time = int(time.time())
    time_elasped = current_time-start_time
    return "Time Elapsed = "+str(time_elasped)+" sec"


####################################################################################################################
'''
#These three functions are used to draw the ghost
def draw_ghost(screen, pos):
	pixels = pixels_from_points(pos)
	screen.blit(pygame.transform.scale(ghostimage, (25, 25)), pixels)
def draw_ghost2(screen, pos):
	pixels = pixels_from_points(pos)
	screen.blit(pygame.transform.scale(ghostimage2, (25, 25)), pixels)
def draw_ghost3(screen, pos):
	pixels = pixels_from_points(pos)
	screen.blit(pygame.transform.scale(ghostimage3, (25, 25)), pixels)
'''


###################################################################################################################


def change_the_direction_of_ghost(move_direction_of_ghost):
    '''
    This function is used to change the direction of ghost
    whenever a wall is faced by ghost this function is called and it randonmly decides the new directions of ghost
    Return - the new direction in which ghost should move
    '''
    position_to_decide = random.randint(0, 3)
    if(position_to_decide == 0):
        move_direction_of_ghost = TOP
    elif(position_to_decide == 1):
        move_direction_of_ghost = DOWN
    elif(position_to_decide == 2):
        move_direction_of_ghost = RIGHT
    elif(position_to_decide == 3):
        move_direction_of_ghost = LEFT
    return move_direction_of_ghost


counter_to_maintain_pacman_animation = 0

# Initializing pygame
pygame.init()
pygame.font.init()


# For loading images and font

font = pygame.font.SysFont('Comic Sans MS', 15)
bigfont = pygame.font.SysFont('Comic Sans MS', 50)
myimage = pygame.image.load(STATIC_DIR + "pacman1.gif")
myimage1 = pygame.image.load(STATIC_DIR + "pacman2.gif")
myimage2 = pygame.image.load(STATIC_DIR + "pacman3.gif")
myimage3 = pygame.image.load(STATIC_DIR + "pacman4.gif")
ghostimage = pygame.image.load(STATIC_DIR + "ghost1.png")
ghostimage2 = pygame.image.load(STATIC_DIR + "ghost2.png")
ghostimage3 = pygame.image.load(STATIC_DIR + "ghost3.png")


# Width and height of the window
screen = pygame.display.set_mode((800, 640), 0, 32)
pygame.display.set_caption("Pacman -  Created By Archit Agrawal")
background = pygame.surface.Surface((800, 800)).convert()


# Initializing variables

layout = loadtxt('layout.txt', dtype=str)
# pygame.mixer.music.load('starting.mp3')
# pygame.mixer.music.play(0)
rows, cols = layout.shape
# Sprint(rows,cols)
pacman_position = (1, 1)

background.fill((0, 0, 0))


'''
ghost1_position=(8,10)
ghost2_position=(9,10)
ghost3_position=(10,10)
'''

ghost1 = ghostclass(8, 10, [1, 0])
ghost2 = ghostclass(9, 10, [1, 0])
ghost3 = ghostclass(10, 10, [1, 0])


# To initialise the value of score and time and the direction

current_score = 0
lives_left = 3
start_time = int(time.time())
angle_where_pacman_point = 0


move_direction = [0, 0]

check_for_level_2 = 1

cheat_code = 0  # Cheatcode is ppppp

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0, 0))

    ghost1_position = ghost1.ghostposition()
    ghost2_position = ghost2.ghostposition()
    ghost3_position = ghost3.ghostposition()

    move_direction_of_ghost1 = ghost1.find_move_direction()
    move_direction_of_ghost2 = ghost2.find_move_direction()
    move_direction_of_ghost3 = ghost3.find_move_direction()

    # The Part to teleport the player to next level
    if(check_for_level_2 == 1):
        if(current_score == 152):
            leveldisplayed = " LEVEL - 2 "
            textsurface = bigfont.render(
                leveldisplayed, False, (255, 255, 255))
            screen.blit(textsurface, (220, 300))
            pygame.display.update()
            time.sleep(2)
            layout = loadtxt('layout2.txt', dtype=str)
            # pygame.mixer.music.load('starting.mp3')
            # pygame.mixer.music.play(0)
            # Back to Initial state
            check_for_level_2 = 3

            current_score = 0
            pacman_position = (1, 1)
            ghost1_position = (9, 10)
            ghost2_position = (9, 10)
            ghost3_position = (9, 10)

    # 182
    if(current_score == 182 or cheat_code == 5):
        leveldisplayed = " Congratulations You Won "
        textsurface = bigfont.render(leveldisplayed, False, (255, 255, 255))
        screen.blit(textsurface, (110, 200))
        time_surface = bigfont.render(
            for_displaying_time_elapsed(), False, (255, 255, 255))
        screen.blit(time_surface, (200, 300))
        pygame.display.update()
        time.sleep(5)
        exit()

    # Draw board from the 2d layout array.
   # In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
    for col in range(cols):
        for row in range(rows):
            value = layout[row][col]
            pos = (col, row)
            if value == 'w':
                draw_wall(screen, pos)
            elif value == 'c':
                draw_coin(screen, pos)

    if lives_left == 0:
        livessurface = bigfont.render("You Died", False, (255, 255, 255))
        screen.blit(livessurface, (300, 300))
        pygame.display.update()
        time.sleep(5)
        exit()

    # Draw the player and ghost
    draw_pacman(screen, pacman_position, angle_where_pacman_point)

    ghost1.draw_ghost(screen, 1)
    ghost2.draw_ghost(screen, 2)
    ghost3.draw_ghost(screen, 3)

    '''
	draw_ghost(screen,ghost1_position)
	draw_ghost2(screen,ghost2_position)
	draw_ghost3(screen,ghost3_position)

	'''

    counter_to_maintain_pacman_animation += 1

    # If ghost touch pacman then you lose a life and pacman gets responed to start point
    if(pacman_position == ghost1_position or pacman_position == ghost2_position or pacman_position == ghost3_position):
        pygame.display.update()
        pacman_position = (1, 1)
        lives_left = lives_left-1
        livessurface = bigfont.render(
            "You Lost a Life", False, (255, 255, 255))
        screen.blit(livessurface, (300, 300))
        pygame.display.update()
        # pygame.mixer.music.load('crash.mp3')
        # pygame.mixer.music.play(0)
        time.sleep(3)

    # Check what key is pressed and chage the direction accordingly
    key_currently_pressed = pygame.key.get_pressed()

    if key_currently_pressed[K_d]:
        move_direction = RIGHT
        angle_where_pacman_point = 0
        cheat_code = 0
    if key_currently_pressed[K_w]:
        move_direction = TOP
        angle_where_pacman_point = 90
        cheat_code = 0
    if key_currently_pressed[K_s]:
        move_direction = DOWN
        angle_where_pacman_point = 270
        cheat_code = 0
    if key_currently_pressed[K_a]:
        move_direction = LEFT
        angle_where_pacman_point = 180
        cheat_code = 0

    #######################################################
    # cheat code
    if key_currently_pressed[K_p]:
        cheat_code += 1
    else:
        cheat_code = 0
    #################################################

    # Update player position based on movement.
    previous_pacman_position = pacman_position

    pacman_position = add_to_pos(pacman_position, move_direction)

    ####
    # For tunneling effect

    if(pacman_position == (19, 10)):
        pacman_position = (0, 10)

    elif(pacman_position == (-1, 10)):
        pacman_position = (18, 10)

    '''
	if (layout[round(pacman_position[1]+0.5)][round(pacman_position[0])]=='w') and move_direction==DOWN:
			pacman_position=previous_pacman_position	
	if (layout[round(pacman_position[1]-0.5)][round(pacman_position[0])]=='w') and move_direction==TOP:
			pacman_position=previous_pacman_position	
	if (layout[round(pacman_position[1])][round(pacman_position[0]-0.5)]=='w') and move_direction==LEFT:
			pacman_position=previous_pacman_position	
	if (layout[round(pacman_position[1])][round(pacman_position[0]+0.5)]=='w') and move_direction==RIGHT:
			pacman_position=previous_pacman_position	


	
	'''

    # if(angle_where_pacman_point==0):
    # or layout[floor(pacman_position[1])][ceil(pacman_position[0])]=='w') : #movig along column
    if (layout[pacman_position[1]][pacman_position[0]] == 'w'):
        pacman_position = previous_pacman_position
    '''
	elif(angle_where_pacman_point==180):
		if ( layout[int(floor(pacman_position[1]))][int(floor(pacman_position[0]))]=='w' or layout[int(ceil(pacman_position[1]))][int(floor(pacman_position[0]))]=='w') :
			pacman_position=previous_pacman_position		
	
	elif(angle_where_pacman_point==270):
		if (layout[int(ceil(pacman_position[1]))][int(pacman_position[0])]=='w'):# or layout[int(ceil(pacman_position[1]))][int(floor(pacman_position[0]))]=='w'):
			pacman_position=previous_pacman_position


	else:
		if(layout[int(floor(pacman_position[1]))][int(floor(pacman_position[0]))]=='w' or layout[int(floor(pacman_position[1]))][int(pacman_position[0])]=='w' ) :
			pacman_position=previous_pacman_position	
	'''

    #######################################################################################################################

    # Ghost section
    # Condition to check if pacman and ghost touch

    previous_ghost1_position = ghost1_position
    previous_ghost2_position = ghost2_position
    previous_ghost3_position = ghost3_position

    if(pacman_position == ghost1_position or pacman_position == ghost2_position or pacman_position == ghost3_position):
        pass
    else:											# For moving ghost
        ghost1_position = add_to_pos(ghost1_position, move_direction_of_ghost1)
        ghost2_position = add_to_pos(ghost2_position, move_direction_of_ghost2)
        ghost3_position = add_to_pos(ghost3_position, move_direction_of_ghost3)

    # Condition for checking if ghost clash with wall or So it will change its direction

    if(layout[round(ghost1_position[1])][round(ghost1_position[0])] == 'w'):
        ghost1_position = previous_ghost1_position
        move_direction_of_ghost1 = change_the_direction_of_ghost(
            move_direction_of_ghost1)

    if(layout[round(ghost2_position[1])][round(ghost2_position[0])] == 'w'):
        ghost2_position = previous_ghost2_position
        move_direction_of_ghost2 = change_the_direction_of_ghost(
            move_direction_of_ghost2)

    if(layout[round(ghost3_position[1])][round(ghost3_position[0])] == 'w'):
        ghost3_position = previous_ghost3_position
        move_direction_of_ghost3 = change_the_direction_of_ghost(
            move_direction_of_ghost3)

    # Coin collection area
    if (layout[int(pacman_position[1])][int(pacman_position[0])] == 'c'):
        current_score = current_score+1  # Updating the score
        layout[int(pacman_position[1])][int(
            pacman_position[0])] = '.'  # Removing the coin

    # For displaying score and time and lives left

    #############################################################

    time_surface = font.render(
        for_displaying_time_elapsed(), False, (255, 255, 255))
    screen.blit(time_surface, (620, 300))

    the_score_to_be_displayed = "Your Score = "+str(current_score)
    textsurface = font.render(
        the_score_to_be_displayed, False, (255, 255, 255))
    screen.blit(textsurface, (620, 200))

    life_to_display = "Lives left = "+str(lives_left)
    livessurface = font.render(life_to_display, False, (255, 255, 255))
    screen.blit(livessurface, (620, 400))

    # TODO: Check if player ate any coin, or collided with the wall by using the layout array.

    # Update the display

    ghost1.updateposition(ghost1_position)
    ghost2.updateposition(ghost2_position)
    ghost3.updateposition(ghost3_position)

    ghost1.update_move_direction(move_direction_of_ghost1)
    ghost2.update_move_direction(move_direction_of_ghost2)
    ghost3.update_move_direction(move_direction_of_ghost3)

    pygame.display.update()

    # Wait for a while, computers are very fast.
    time.sleep(0.2)


###############################################################
# The end
