from pythonpackages.renpygame.display import Surface
from pythonpackages.renpygame_pygame.draw import *
import pythonpackages.renpygame_pygame as pygame
import renpy.exports as renpy

# https://www.pygame.org/docs/ref/draw.html
# https://www.renpy.org/doc/html/cdd.html#renpy.Render.canvas
# https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1610


def rect(
    surface: Surface,
    color,
    rect,
    width=0,
    border_radius=0,
    border_top_left_radius=-1,
    border_top_right_radius=-1,
    border_bottom_left_radius=-1,
    border_bottom_right_radius=-1,
) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect"""
    canvas = surface.canvas()
    return canvas.rect(color, rect, width)


def polygon(surface, color, points, width=0) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon"""
    canvas = surface.canvas()
    return canvas.polygon(color, points, width)


def circle(
    surface,
    color,
    center,
    radius,
    width=0,
    draw_top_right=None,
    draw_top_left=None,
    draw_bottom_left=None,
    draw_bottom_right=None,
) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle"""
    canvas = surface.canvas()
    return canvas.circle(color, center, radius, width)


def ellipse(surface, color, rect, width=0) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse"""
    canvas = surface.canvas()
    return canvas.ellipse(color, rect, width)


def arc(surface, color, rect, start_angle, stop_angle, width=1) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc"""
    canvas = surface.canvas()
    return canvas.arc(color, rect, start_angle, stop_angle, width)


def line(surface, color, start_pos, end_pos, width=1) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.line"""
    canvas = surface.canvas()
    return canvas.line(color, start_pos, end_pos, width)


def lines(surface, color, closed, pointlist, width=1) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines"""
    canvas = surface.canvas()
    return canvas.lines(color, closed, pointlist, width)


def aaline(surface, color, startpos, endpos, blend=1) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.aaline"""
    canvas = surface.canvas()
    return canvas.aaline(color, startpos, endpos, blend)


def aalines(surface, color, closed, pointlist, blend=1) -> pygame.Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.aalines"""
    canvas = surface.canvas()
    return canvas.aalines(color, closed, pointlist, blend)
