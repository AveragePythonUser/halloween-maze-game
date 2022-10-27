import pygame, os

ghost_img = pygame.image.load(os.path.join("assets/ghost.png"))

ghost_pos = [0, 0]
ghost_rect = pygame.Rect(0, 0, 32,32)
trans_surf = pygame.Surface((256,256)) # i have to make a seperate surface if i want anything to be transparent because pygame draw function doesnt support it
trans_surf.set_alpha(50) # sets alpha value (aka makes slightly transparent)
speed = 2

def move(DISPLAY, player_rect, scroll):
    trans_surf.fill((0,0,0))
    ghost_rect.x = ghost_pos[0] - scroll[0]
    ghost_rect.y = ghost_pos[1] - scroll[1]
    trans_surf.blit(ghost_img, (ghost_rect.x, ghost_rect.y))
    #DISPLAY.blit(trans_surf, (ghost_pos[0] - scroll[0], ghost_pos[1] - scroll[1]))
    DISPLAY.blit(trans_surf, (0, 0))
    if player_rect.x > ghost_rect.x:
        ghost_pos[0] += speed
    elif player_rect.x < ghost_rect.x:
        ghost_pos[0] -= speed
    if player_rect.y > ghost_rect.y:
        ghost_pos[1] += speed
    elif player_rect.y < ghost_rect.y:
        ghost_pos[1] -= speed