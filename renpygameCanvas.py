import renpy.exports as renpy


class Canvas(renpy.display.render.Canvas):
    """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1610"""

    def __init__(self, surf):
        # renpy.display.Canvas init
        super().__init__(surf)
