from pythonpackages.renpygame_pygame.draw import *
import renpy.exports as renpy

# https://www.pygame.org/docs/ref/draw.html
# https://www.renpy.org/doc/html/cdd.html#renpy.Render.canvas
# https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1610


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
):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect"""
    canvas = surface.canvas()
    canvas.rect(color, rect, width)
    return surface


def polygon(surface, color, points, width=0):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.polygon"""
    canvas = surface.canvas()
    canvas.polygon(color, points, width)
    return surface


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
):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle"""
    canvas = surface.canvas()
    canvas.circle(color, center, radius, width)
    return canvas.get_surface().get_rect()


def ellipse(surface, color, rect, width=0):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.ellipse"""
    canvas = surface.canvas()
    canvas.ellipse(color, rect, width)
    return surface


def arc(surface, color, rect, start_angle, stop_angle, width=1):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc"""
    canvas = surface.canvas()
    canvas.arc(color, rect, start_angle, stop_angle, width)
    return surface


def line(surface, color, start_pos, end_pos, width=1):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.line"""
    canvas = surface.canvas()
    canvas.line(color, start_pos, end_pos, width)
    return surface


def lines(surface, color, closed, pointlist, width=1):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines"""
    canvas = surface.canvas()
    canvas.lines(color, closed, pointlist, width)
    return surface


def aaline(surface, color, startpos, endpos, blend=1):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.aaline"""
    canvas = surface.canvas()
    canvas.aaline(color, startpos, endpos, blend)
    return surface


def aalines(surface, color, closed, pointlist, blend=1):
    """https://www.pygame.org/docs/ref/draw.html#pygame.draw.aalines"""
    canvas = surface.canvas()
    canvas.aalines(color, closed, pointlist, blend)
    return surface
