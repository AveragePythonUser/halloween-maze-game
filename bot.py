import pygame, random

# -=================================-
#
#    (most) everything to do with the bot 
#    currently unused
# 
# -=================================-

speed = 1
directions = {"up": False, "left": False, "down": False, "right": False}
prev_directions = {"up": True, "left": True, "down": True, "right": True}
#prev_directions = {"up": False, "left": False, "down": False, "right": False}
bot_pos = [32, 64]
bot_rect = pygame.Rect(bot_pos[0], bot_pos[1], 32, 32)
invis_surf = pygame.Surface((16, 16))
invis_surf.set_alpha(50)
last_node = -1
moving = False

collide_rects = []
  
def start(nodes):
    for node in nodes:
        print(node)
        if bot_rect.colliderect(node):
            start_node = node
            bot_pos[0] = start_node.x - 14
            bot_pos[1] = start_node.y - 16
            break
            last_node = bot_rect.collidelist(nodes)
    x = 32
    for i in range(2):
        collide_rects.append(pygame.Rect(bot_pos[0] + x, bot_pos[1], 32, 1))
        x = -32
      
    y = 32
    for i in range(2):
        collide_rects.append(pygame.Rect(bot_pos[0], bot_pos[1], 1, 32))
        y = -32

def change_prev_direct(current): # makes a previous direction so the bot doesnt repeat itself on movement
    prev_directions["up"] = True
    prev_directions["down"] = True
    prev_directions["left"] = True
    prev_directions["right"] = True
    print(current)
    prev_directions[current] = False
      
def rect_scroll(scroll):
    collide_rects[0].x = bot_pos[0] - scroll[0] + 17 
    collide_rects[0].y = bot_pos[1] - scroll[1] + 16

    collide_rects[1].x = bot_pos[0] - scroll[0] - 17 
    collide_rects[1].y = bot_pos[1] - scroll[1] + 16
  
    collide_rects[2].x = bot_pos[0] - scroll[0] + 16 
    collide_rects[2].y = bot_pos[1] - scroll[1] - 17

    collide_rects[3].x = bot_pos[0] - scroll[0] + 16 
    collide_rects[3].y = bot_pos[1] - scroll[1] + 17

def get_direction(direction, wall_rects):
    global moving
    if direction.collidelist(wall_rects) == -1:
        if(direction == collide_rects[0]) and (directions["right"] != prev_directions["right"]):
            moving = True
            directions["right"] = True
            change_prev_direct("left")
        elif(direction == collide_rects[1]) and (directions["left"] != prev_directions["left"]):
            moving = True
            directions["left"] = True
            change_prev_direct("right")
        elif(directions == collide_rects[2]) and (directions["up"] != prev_directions["up"]):
            moving = True
            directions["up"] = True
            change_prev_direct("down")
        elif(direction == collide_rects[3]) and (directions["down"] != prev_directions["down"]):
            moving = True
            directions["down"] = True
            change_prev_direct("up")

def check_direct(wall_rects):
    global moving
    if(directions["right"] == True and collide_rects[0].collidelist(wall_rects) != -1):
      directions["right"] = False
      moving = False
    if(directions["left"] == True and collide_rects[1].collidelist(wall_rects) != -1):
      directions["left"] = False
      moving = False
    if(directions["up"] == True and collide_rects[2].collidelist(wall_rects) != -1):
      directions["up"] = False
      moving = False
    if(directions["down"] == True and collide_rects[3].collidelist(wall_rects) != -1):
      directions["down"] = False
      moving = False

def move_x(speed):
    bot_pos[0] += speed
def move_y(speed):
    bot_pos[1] += speed
  
# rays[4] is middle one (dont use)
def move(dirt_rects, wall_rects, DISPLAY, scroll, nodes):
    global moving
    rect_scroll(scroll)
    for rect in collide_rects:
        pygame.draw.rect(DISPLAY, (255,255,0), rect)
    pygame.draw.rect(DISPLAY, (0,0,255), collide_rects[2])

    available_direct = []
    for line in collide_rects:
        if(line.collidelist(wall_rects) == -1):
            available_direct.append(line)
          
    if moving == False:
        direction = random.choice(collide_rects)
        get_direction(direction, wall_rects)

      
    if moving == True:
        check_direct(wall_rects)
        # print(directions)
        # print(prev_directions)
        if(directions["right"] == True):
            move_x(speed)
        elif(directions["down"] == True):
            move_y(speed)
        elif(directions["up"] == True):
            print('up')
            move_y(-speed)
        elif(directions["left"] == True):
            move_x(-speed)
    elif moving == False:
        pass
        

    
      
            
            
