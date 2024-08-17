from mcpi.minecraft import Minecraft
import param_MCJE1122 as param
import pygame
import time

mc = Minecraft.create()

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

"ここで車をカスタムできます"
"タイヤ"
tire = param.WOOL, 15
"ボディ1"
body1 = param.STONE_SLAB, 11
"ボディ2"
body2 = param.WOOD, 4
"ボディ3"
body3 = param.STAIRS_WOOD,  5
"ボディ4"
body4 = param.WOOD_PLANKS

body5 = param.STONE_SLAB


gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 64)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    message_display('You Crashed')

x = 0
y = 0

def game_loop():
    x = 0
    y = 0

    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            mc.setBlocks(y+5, 8, 4, y-5, 4, -4, param.AIR)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = 0.2
                if event.key == pygame.K_DOWN:
                    y_change = -0.2
            mc.setBlocks(y+5, 8, 4, y-5, 4, -4, param.AIR)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                
        y += y_change            
        
        mc.setBlocks(y+5, 8, 4, y-5, 4, -4, param.AIR)

        gameDisplay.fill(white)

        mc.setBlock(y+1, 4, 1,  tire)
        mc.setBlock(y+1, 4, -1,  tire)
        mc.setBlock(y-2, 4, 1,  tire)
        mc.setBlock(y-2, 4, -1,  tire)
        mc.setBlocks(y-3, 4, -1, y-3, 4, 1,  body1)
        mc.setBlocks(y, 4, -1, y-1, 4, 1,  body1)
        mc.setBlocks(y+2, 4, -1, y+2, 4, 1,  body1)
        mc.setBlocks(y+1, 4, 0, y-2, 4, 0,  body1)
        mc.setBlocks(y+2, 5, -1, y-3, 5, -1,  body2)
        mc.setBlocks(y+2, 5, 1, y-3, 5, 1,  body2)
        mc.setBlock(y+2, 5, 0,  body3)
        mc.setBlock(y-3, 5, 0,  body3)
        mc.setBlocks(y+1, 6, 1, y+1, 6, -1,  param.GLASS)
        mc.setBlock(y-1, 6, 1,  param.GLASS)
        mc.setBlock(y-1, 6, -1,  param.GLASS)
        mc.setBlocks(y-2, 6, 1, y-2, 6, -1,  body4)
        mc.setBlock(y, 6, 1,  body4)
        mc.setBlock(y, 6, -1,  body4)
        mc.setBlocks(y, 7, 1, y-2, 7, -1,  body5)

        pygame.display.update()
        clock.tick(60)

mc.postToChat("car move")


game_loop()
pygame.quit()
quit()

