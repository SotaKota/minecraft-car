from mcje.minecraft import Minecraft
import param_MCJE as param
import pygame
from pygame.locals import Rect

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('時計をつくるで')

# ドットを描く
mc.setBlock(self.screen, param.GOLD_BLOCK, Rect(org1[0], org1[1], block_size, block_size))
i += 1