from pythonpackages.renpygame_pygame.draw import *
from pythonpackages.renpygame.rect import Rect

# https://www.pygame.org/docs/ref/draw.html


def rect(
    surface,
    color,
    rect,
    width=0,
    border_radius=0,
    border_top_left_radius=-1,
    border_top_right_radius=-1,
    border_bottom_left_radius=-1,
    border_bottom_right_radius=-1,
) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect"""
    return


def polygon(surface, color, points, width=0) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon"""
    return


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
) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle"""
    return


def ellipse(surface, color, rect, width=0) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse"""
    return


def arc(surface, color, rect, start_angle, stop_angle, width=1) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc"""
    return


def line(surface, color, start_pos, end_pos, width=1) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.line"""
    return


def lines(surface, color, closed, pointlist, width=1) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines"""
    return


def aaline(surface, color, startpos, endpos, blend=1) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.aaline"""
    return


def aalines(surface, color, closed, pointlist, blend=1) -> Rect:
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.aalines"""
    return
