import pythonpackages.renpygame.display as my_display
import pythonpackages.renpygame.draw as my_draw
import pythonpackages.renpygame.event as my_event
import pythonpackages.renpygame.image as my_image
import pythonpackages.renpygame.mixer as my_mixer
import pythonpackages.renpygame.rect as my_rect
import pythonpackages.renpygame.sprite as my_sprite
import pythonpackages.renpygame.transform as my_transform
from pythonpackages.renpygame.renpygameCDD import (
    RenpyGameByEvent as my_RenpyGameByEvent,
    RenpyGameByTimerForDraw as my_RenpyGameByTimerOnlyDraw,
)
from pythonpackages.renpygame.renpygameCDD import RenpyGameByLoop as my_RenpyGameByLoop
from pythonpackages.renpygame.renpygameCDD import (
    RenpyGameByTimer as my_RenpyGameByTimer,
)
from pythonpackages.renpygame_pygame import *
import pythonpackages.renpygame_pygame as my_pygame

Surface = my_display.Surface
Rect = my_rect.Rect
rect = my_rect
display = my_display
sprite = my_sprite
image = my_image
transform = my_transform
event = my_event
mixer = my_mixer
draw = my_draw

RenpyGameByTimer = my_RenpyGameByTimer
RenpyGameByEvent = my_RenpyGameByEvent
RenpyGameByTimerForDraw = my_RenpyGameByTimerOnlyDraw
RenpyGameByLoop = my_RenpyGameByLoop


def init():
    return


# Event List
QUIT = my_pygame.QUIT
ACTIVEEVENT = my_pygame.ACTIVEEVENT
KEYDOWN = my_pygame.KEYDOWN
KEYUP = my_pygame.KEYUP
MOUSEMOTION = my_pygame.MOUSEMOTION
MOUSEBUTTONUP = my_pygame.MOUSEBUTTONUP
MOUSEBUTTONDOWN = my_pygame.MOUSEBUTTONDOWN
JOYAXISMOTION = my_pygame.JOYAXISMOTION
JOYBALLMOTION = my_pygame.JOYBALLMOTION
JOYHATMOTION = my_pygame.JOYHATMOTION
JOYBUTTONUP = my_pygame.JOYBUTTONUP
JOYBUTTONDOWN = my_pygame.JOYBUTTONDOWN
VIDEORESIZE = my_pygame.VIDEORESIZE
VIDEOEXPOSE = my_pygame.VIDEOEXPOSE
USEREVENT = my_pygame.USEREVENT
