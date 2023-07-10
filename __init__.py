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


# Keyboard list
K_BACKSPACE = my_pygame.K_BACKSPACE
K_TAB = my_pygame.K_TAB
K_CLEAR = my_pygame.K_CLEAR
K_RETURN = my_pygame.K_RETURN
K_PAUSE = my_pygame.K_PAUSE
K_ESCAPE = my_pygame.K_ESCAPE
K_SPACE = my_pygame.K_SPACE
K_EXCLAIM = my_pygame.K_EXCLAIM
K_QUOTEDBL = my_pygame.K_QUOTEDBL
K_HASH = my_pygame.K_HASH
K_DOLLAR = my_pygame.K_DOLLAR
K_AMPERSAND = my_pygame.K_AMPERSAND
K_QUOTE = my_pygame.K_QUOTE
K_LEFTPAREN = my_pygame.K_LEFTPAREN
K_RIGHTPAREN = my_pygame.K_RIGHTPAREN
K_ASTERISK = my_pygame.K_ASTERISK
K_PLUS = my_pygame.K_PLUS
K_COMMA = my_pygame.K_COMMA
K_MINUS = my_pygame.K_MINUS
K_PERIOD = my_pygame.K_PERIOD
K_SLASH = my_pygame.K_SLASH
K_0 = my_pygame.K_0
K_1 = my_pygame.K_1
K_2 = my_pygame.K_2
K_3 = my_pygame.K_3
K_4 = my_pygame.K_4
K_5 = my_pygame.K_5
K_6 = my_pygame.K_6
K_7 = my_pygame.K_7
K_8 = my_pygame.K_8
K_9 = my_pygame.K_9
K_COLON = my_pygame.K_COLON
K_SEMICOLON = my_pygame.K_SEMICOLON
K_LESS = my_pygame.K_LESS
K_EQUALS = my_pygame.K_EQUALS
K_GREATER = my_pygame.K_GREATER
K_QUESTION = my_pygame.K_QUESTION
K_AT = my_pygame.K_AT
K_LEFTBRACKET = my_pygame.K_LEFTBRACKET
K_BACKSLASH = my_pygame.K_BACKSLASH
K_RIGHTBRACKET = my_pygame.K_RIGHTBRACKET
K_CARET = my_pygame.K_CARET
K_UNDERSCORE = my_pygame.K_UNDERSCORE
K_BACKQUOTE = my_pygame.K_BACKQUOTE
K_a = my_pygame.K_a
K_b = my_pygame.K_b
K_c = my_pygame.K_c
K_d = my_pygame.K_d
K_e = my_pygame.K_e
K_f = my_pygame.K_f
K_g = my_pygame.K_g
K_h = my_pygame.K_h
K_i = my_pygame.K_i
K_j = my_pygame.K_j
K_k = my_pygame.K_k
K_l = my_pygame.K_l
K_m = my_pygame.K_m
K_n = my_pygame.K_n
K_o = my_pygame.K_o
K_p = my_pygame.K_p
K_q = my_pygame.K_q
K_r = my_pygame.K_r
K_s = my_pygame.K_s
K_t = my_pygame.K_t
K_u = my_pygame.K_u
K_v = my_pygame.K_v
K_w = my_pygame.K_w
K_x = my_pygame.K_x
K_y = my_pygame.K_y
K_z = my_pygame.K_z
K_DELETE = my_pygame.K_DELETE
K_KP0 = my_pygame.K_KP0
K_KP1 = my_pygame.K_KP1
K_KP2 = my_pygame.K_KP2
K_KP3 = my_pygame.K_KP3
K_KP4 = my_pygame.K_KP4
K_KP5 = my_pygame.K_KP5
K_KP6 = my_pygame.K_KP6
K_KP7 = my_pygame.K_KP7
K_KP8 = my_pygame.K_KP8
K_KP9 = my_pygame.K_KP9
K_KP_PERIOD = my_pygame.K_KP_PERIOD
K_KP_DIVIDE = my_pygame.K_KP_DIVIDE
K_KP_MULTIPLY = my_pygame.K_KP_MULTIPLY
K_KP_MINUS = my_pygame.K_KP_MINUS
K_KP_PLUS = my_pygame.K_KP_PLUS
K_KP_ENTER = my_pygame.K_KP_ENTER
K_KP_EQUALS = my_pygame.K_KP_EQUALS
K_UP = my_pygame.K_UP
K_DOWN = my_pygame.K_DOWN
K_RIGHT = my_pygame.K_RIGHT
K_LEFT = my_pygame.K_LEFT
K_INSERT = my_pygame.K_INSERT
K_HOME = my_pygame.K_HOME
K_END = my_pygame.K_END
K_PAGEUP = my_pygame.K_PAGEUP
K_PAGEDOWN = my_pygame.K_PAGEDOWN
K_F1 = my_pygame.K_F1
K_F2 = my_pygame.K_F2
K_F3 = my_pygame.K_F3
K_F4 = my_pygame.K_F4
K_F5 = my_pygame.K_F5
K_F6 = my_pygame.K_F6
K_F7 = my_pygame.K_F7
K_F8 = my_pygame.K_F8
K_F9 = my_pygame.K_F9
K_F10 = my_pygame.K_F10
K_F11 = my_pygame.K_F11
K_F12 = my_pygame.K_F12
K_F13 = my_pygame.K_F13
K_F14 = my_pygame.K_F14
K_F15 = my_pygame.K_F15
K_NUMLOCK = my_pygame.K_NUMLOCK
K_CAPSLOCK = my_pygame.K_CAPSLOCK
K_SCROLLOCK = my_pygame.K_SCROLLOCK
K_RSHIFT = my_pygame.K_RSHIFT
K_LSHIFT = my_pygame.K_LSHIFT
K_RCTRL = my_pygame.K_RCTRL
K_LCTRL = my_pygame.K_LCTRL
K_RALT = my_pygame.K_RALT
K_LALT = my_pygame.K_LALT
K_RMETA = my_pygame.K_RMETA
K_LMETA = my_pygame.K_LMETA
K_LSUPER = my_pygame.K_LSUPER
K_RSUPER = my_pygame.K_RSUPER
K_MODE = my_pygame.K_MODE
K_HELP = my_pygame.K_HELP
K_PRINT = my_pygame.K_PRINT
K_SYSREQ = my_pygame.K_SYSREQ
K_BREAK = my_pygame.K_BREAK
K_MENU = my_pygame.K_MENU
K_POWER = my_pygame.K_POWER
K_EURO = my_pygame.K_EURO
K_AC_BACK = my_pygame.K_AC_BACK
