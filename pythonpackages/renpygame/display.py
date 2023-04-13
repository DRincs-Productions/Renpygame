from typing import Any, Optional, Union
import renpy.exports as renpy
from pygame_sdl2.display import *

import pythonpackages.renpygame.pygame as pygame
import pythonpackages.renpygame.image as my_image


class RenpyGameSurface(renpy.Displayable):
    def __init__(self, **kwargs):
        # renpy.Displayable init
        super(RenpyGameSurface, self).__init__(**kwargs)

        self.renderMainSurface = renpy.Render(300, 300)

    def render(self, width, height, st, at) -> renpy.Render:
        # Create the render we will return.
        render = renpy.Render(width, width)

        # Create a render from the child.
        # child_render = renpy.render(renpy.displayable(
        #     "background.gif"), width, height, st, at)

        file = renpy.open_file("images/background.gif")
        image = pygame.image.load(file)
        bgdtile = image.convert()
        # bgdtile = renpy.displayable("background.gif")

        background = pygame.Surface((300, 300))
        background.blit(bgdtile, (300, 300))
        # child_render.blit(background, (300, 300))

        # Get the size of the child.
        # self.width, self.height = child_render.get_size()

        # Blit (draw) the child's render to our render.
        render.blit(background, (0, 0))

        # Return the render.
        return render


def set_mode(size: tuple[int, int] = (0, 0), flags: int = 0, depth: int = 0, display: int = 0, vsync: int = 0) -> RenpyGameSurface:
    """If it is commented out it will replace the renpy screen creating an error when returning to renpy. https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode"""
    # * It has the job of replacing the original so nothing happens
    surface = RenpyGameSurface()
    # renpy.show_screen("renpygame_surface", surface=surface)
    return surface


def mode_ok(size: tuple[int, int], flags: int = 0, depth: int = 0, display: int = 0) -> int:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.mode_ok"""
    return pygame.display.mode_ok(size, flags, depth)


def set_icon(Surface) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon"""
    return pygame.display.set_icon(Surface)


def flip() -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.flip"""
    return pygame.display.flip()


def update(rectangle: Optional[Union[list, Any]] = None) -> None:
    """https://www.pygame.org/docs/ref/display.html#pygame.display.update"""
    return pygame.display.update(rectangle)
