import pygame, sys, os, time
from pygame.locals import QUIT
import ghost
from ghost import ghost_rect as ghost_rect

pygame.init()
WIDTH, HEIGHT = 256 * 2, 256 * 2
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("spooky")
DISPLAY = pygame.Surface((WIDTH / 2, HEIGHT / 2))

assets = os.path.join("assets")

DIRT = pygame.image.load(os.path.join(assets, "dirt.png"))
WALL = pygame.image.load(os.path.join(assets, "brick.png"))
SHADOW = pygame.image.load(os.path.join(assets, "shadow.png"))
PLAYER = pygame.image.load(os.path.join(assets, "player.png"))
RUBY = pygame.image.load(os.path.join(assets, "ruby_spook.png"))
BOT_IMG = False 


shadow_surf = pygame.Surface((WIDTH / 2, HEIGHT / 2))

shadow_surf.set_alpha(35)


CLOCK = pygame.time.Clock()
FPS = 60

dirt_rects = []
wall_rects = []
nodes = []
lines = []
win_rects = []

true_scroll = [0, 0]
scroll = [0,0]

player_pos = [32, 64] # stores the position of the player in a rect to be refenced later
player_rect = pygame.Rect(player_pos[0], player_pos[1], 32, 32)

render_rect = pygame.Rect(0,0, WIDTH / 2, HEIGHT /2)

speed = 3

def load_map(path):
    f = open(path + '.txt', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map("maze") # loads game_map as a list into ram
background = load_map("background") # unused 

def initialize_map():
    
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if(tile == "1"):
                DISPLAY.blit(WALL, tile_pos(x, y, "n"))
                wall_rect = pygame.Rect(x * 32 - scroll[0], y * 32 - scroll[1], 32, 32)
                wall_rects.append(wall_rect)
                
            if(tile == "0"):
                DISPLAY.blit(DIRT, tile_pos(x, y, "n"))
                dirt_rect = pygame.Rect(x * 32, y * 32, 32, 32)
                dirt_rects.append(dirt_rect) # remove later maybe
            if(tile == "!"):
                node = pygame.Rect(x * 32 + 28 - scroll[0], y * 32 - scroll[1], 4, 4)
                nodes.append(node)
                DISPLAY.blit(DIRT, tile_pos(x, y , "n"))
                             
            x += 1
        y += 1

    # mapping = True

    # line_direction = {"up": False, "left": False, "down": False, "right": False}

    # while mapping == True:
    #     line = pygame.draw.line(DISPLAY, (255,255,0), (nodes[0].x + 4, nodes[0].y - 2), (nodes[0].x, nodes[0].y))
    #     for rect in nodes:
    #         if(line.colliderect(rect)):
    #             lines.append(line)
    #             mapping = False
    #             break
    #         else:
    #             line.width += 32
                

def tile_pos(x, y, type):
    if (type == "n"): # is effected by scroll
        return x * 32 - scroll[0], y * 32 - scroll[1] 
    elif(type == "b"): # is not effected by scroll
        return x * 32, y * 32

def k_player_up(speed):
    player_pos[1] -= speed # player_pos[1] refers to the players y position

def k_player_left(speed):
    player_pos[0] -= speed # player_pos[0] refers to the players x position
  
def k_player_down(speed):
    player_pos[1] += speed

def k_player_right(speed):
    player_pos[0] += speed


def movement(key_pressed, l_speed):
    if(key_pressed [pygame.K_UP]) or (key_pressed [pygame.K_w]): # UP
        k_player_up(l_speed)
    if(key_pressed [pygame.K_LEFT]) or (key_pressed [pygame.K_a]): # LEFT
        k_player_left(l_speed)
    if(key_pressed [pygame.K_DOWN]) or (key_pressed [pygame.K_s]): # DOWN
        k_player_down(l_speed)
    if(key_pressed [pygame.K_RIGHT]) or (key_pressed [pygame.K_d]): # RIGHT
        k_player_right(l_speed)
      
    player_rect.x, player_rect.y = player_pos[0] - scroll[0], player_pos[1] - scroll[1]

def render(dirt_rects, wall_rects):
      
    # RENDERS GAME MAP
    
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if(tile == "1"):
                wall_rect = pygame.Rect(x * 32 - scroll[0], y * 32 - scroll[1], 32, 32)
                wall_rects.append(wall_rect)
                if wall_rect.colliderect(render_rect):
                    DISPLAY.blit(WALL, tile_pos(x, y, "n"))
                  
            if(tile == "0"):
                dirt_rect = pygame.Rect(x * 32 - scroll[0], y * 32 - scroll[1], 32, 32)
                dirt_rects.append(dirt_rect)
                if dirt_rect.colliderect(render_rect):
                    DISPLAY.blit(DIRT, tile_pos(x, y, "n"))
            if(tile == "W"):
                ruby_rect = pygame.Rect(x * 32 - scroll[0], y * 32 - scroll[1], 32, 32 )
                win_rects.append(ruby_rect)
                if ruby_rect.colliderect(render_rect):
                    DISPLAY.blit(DIRT, tile_pos(x, y, "n"))
                    DISPLAY.blit(RUBY, (tile_pos(x, y, "n")))
                             
            x += 1
        y += 1


def player_collision(rect):
    if(key_pressed [pygame.K_UP]) or (key_pressed [pygame.K_w]): # UP
        k_player_up(- speed)
    if(key_pressed [pygame.K_LEFT]) or (key_pressed [pygame.K_a]): # LEFT
        k_player_left(- speed)
    if(key_pressed [pygame.K_DOWN]) or (key_pressed [pygame.K_s]): # DOWN
        k_player_down(- speed)
    if(key_pressed [pygame.K_RIGHT]) or (key_pressed [pygame.K_d]): # RIGHT
        k_player_right(- speed)

def collision(key_pressed, speed):

    for rect in wall_rects:
        rect.x - scroll[0]
        rect.y - scroll[1]
        if(player_rect.colliderect(rect)):
            player_collision(rect)

initialize_map()

while True:
    CLOCK.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

      

    key_pressed = pygame.key.get_pressed()


    DISPLAY.fill((12, 12, 20))

    true_scroll[0] += (player_rect.x - 128 + 16)/20
    true_scroll[1] += (player_rect.y - 128 + 16)/20
    scroll = true_scroll.copy()
    scroll[0] = int(true_scroll[0])
    scroll[1] = int(true_scroll[1])

    dirt_rects = []
    wall_rects = []
    nodes = [] # MAKE SURE TO RESET YOUR LIST OF RECTS 
    win_rects = []
    
    movement(key_pressed, speed)  
    render(dirt_rects, wall_rects)
    collision(key_pressed, speed)  
    ghost.move(DISPLAY, player_rect, scroll)
    #pygame.draw.rect(DISPLAY, (255,0,0), render_rect)

    for line in lines:
        pygame.draw.rect(DISPLAY, (255,255,0), line)
        line.x -= scroll[0]
        line.y -= scroll[1]


    #pygame.draw.rect(DISPLAY, (0,0,255), player_rect)
    #DISPLAY.blit(SHADOW, (player_rect.x - 128 + 16,player_rect.y - 128 + 16)) put in later (also make better shadow)

    DISPLAY.blit(PLAYER, (player_rect.x, player_rect.y))
    surf = pygame.transform.scale(DISPLAY, (HEIGHT, WIDTH))
      
    WIN.blit(surf, (0, 0))
    pygame.display.update()