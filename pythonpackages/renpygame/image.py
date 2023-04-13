import renpy.exports as renpy
from pygame_sdl2.image import *

import pythonpackages.renpygame.pygame as pygame


def load(file) -> pygame.Surface:
    """https://www.pygame.org/docs/ref/image.html#pygame.image.load"""
    image = renpy.displayable(file)
    render = renpy.render(image, 300, 300, 0, 0)
    res = pygame.Surface((300, 300))
    res.blit(render, (0, 0))
    return res
