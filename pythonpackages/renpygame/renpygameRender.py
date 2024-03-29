from typing import Optional
import renpy.exports as renpy

from pythonpackages.renpygame.renpygameCanvas import Canvas


class Render(renpy.Render):
    """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L586
    # TODO there is a problem a problem with self.width and self.height. They are a float and must be an int.
    """

    def __init__(
        self,
        width: int,
        height: int,
    ):
        # renpy.Render init
        super().__init__(width, height)
        # * Render properties, will come set in super().__init__

        self.internal_render = None
        self.background_render = None
        self._renpygame_canvas = None

    @property
    def mark(self):
        return super().mark

    @property
    def cache_killed(self):
        return super().cache_killed

    @property
    def killed(self):
        return super().killed

    @property
    def width(self) -> int:
        """must be int"""
        return int(super().width)

    @width.setter
    def width(self, value: int):
        """must be int.
        # TODO there is a problem a problem with self.width and self.height. They are a float and must be an int.
        """
        super().width = int(value)

    @property
    def height(self) -> int:
        """must be int"""
        return int(super().height)

    @height.setter
    def height(self, value: int):
        """must be int.
        # TODO there is a problem a problem with self.width and self.height. They are a float and must be an int.
        """
        super().height = int(value)
        print("height set to", value)

    @property
    def layer_name(self):
        return super().layer_name

    @property
    def children(self):
        return super().children

    @property
    def forward(self):
        return super().forward

    @property
    def reverse(self):
        return super().reverse

    @property
    def alpha(self):
        return super().alpha

    @property
    def over(self):
        return super().over

    @property
    def nearest(self):
        return super().nearest

    @property
    def focuses(self):
        return super().focuses

    @property
    def pass_focuses(self):
        return super().pass_focuses

    @property
    def focus_screen(self):
        return super().focus_screen

    @property
    def render_of(self):
        return super().render_of

    @property
    def xclipping(self):
        return super().xclipping

    @property
    def yclipping(self):
        return super().yclipping

    @property
    def modal(self):
        return super().modal

    @property
    def text_input(self):
        return super().text_input

    @property
    def parents(self):
        return super().parents

    @property
    def depends_on_list(self):
        return super().depends_on_list

    @property
    def operation(self):
        return super().operation

    @property
    def operation_complete(self):
        return super().operation_complete

    @property
    def operation_alpha(self):
        return super().operation_alpha

    @property
    def operation_parameter(self):
        return super().operation_parameter

    @property
    def surface(self):
        return super().surface

    @property
    def alpha_surface(self):
        return super().alpha_surface

    @property
    def half_cache(self):
        return super().half_cache

    @property
    def mesh(self):
        return super().mesh

    @property
    def shaders(self):
        return super().shaders

    @property
    def uniforms(self):
        return super().uniforms

    @property
    def properties(self):
        return super().properties

    @property
    def cached_texture(self):
        return super().cached_texture

    @property
    def cached_model(self):
        return super().cached_model

    @property
    def loaded(self):
        return super().loaded

    def blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> int:
        """render.blit(): https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L778"""
        if hasattr(source, "background_render") and source.background_render:
            surffill = renpy.render(
                source.background_render, source.width, source.height, 0, 0
            )
            super().blit(surffill, pos, focus, main, index)
        if hasattr(source, "internal_render") and source.internal_render:
            source = source.internal_render
        return super().blit(source, pos, focus, main, index)

    def subpixel_blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> int:
        return super().subpixel_blit(source, pos, focus, main, index)

    def absolute_blit(
        self, source, pos: tuple[int, int], focus=True, main=True, index=None
    ) -> int:
        return super().absolute_blit(source, pos, focus, main, index)

    def get_size(self) -> tuple[int, int]:
        return super().get_size()

    def render_to_texture(self, alpha=True):
        return super().render_to_texture(alpha)

    def subsurface(self, rect, focus=False):
        return super().subsurface(rect, focus)

    def depends_on(self, source, focus=False):
        return super().depends_on(source, focus)

    def kill_cache(self):
        return super().kill_cache()

    def kill(self):
        return super().kill()

    def add_focus(
        self, d, arg=None, x=0, y=0, w=None, h=None, mx=None, my=None, mask=None
    ):
        return super().add_focus(d, arg, x, y, w, h, mx, my, mask)

    def take_focuses(self, cminx, cminy, cmaxx, cmaxy, transform, screen, focuses):
        return super().take_focuses(
            cminx, cminy, cmaxx, cmaxy, transform, screen, focuses
        )

    def focus_at_point(self, x, y, screen):
        return super().focus_at_point(x, y, screen)

    def main_displayables_at_point(self, x, y, layers, depth=None):
        return super().main_displayables_at_point(x, y, layers, depth)

    def is_pixel_opaque(self, x, y):
        return super().is_pixel_opaque(x, y)

    def fill(self, color):
        """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1469
        # TODO there is a problem a problem with self.width and self.height. They are a float and must be an int. so I have overriden this method
        """
        color = renpy.easy.color(color)
        # TODO use a self.background_render si not correct, because the color must blit over the current render and under the current render
        self.background_render = renpy.display.imagelike.Solid(color)
        # self.blit(surf, (0, 0), focus=False, main=False)

        if self.internal_render:
            self.internal_render.fill(color)

        # update the canvas
        if self.renpygame_canvas:
            self.renpygame_canvas = None
            _ = self.renpygame_canvas
        return

    def canvas(self) -> Canvas:
        """https://github.com/renpy/renpy/blob/master/renpy/display/render.pyx#L1480
        # TODO there is a problem a problem with self.width and self.height. They are a float and must be an int. so I have overriden this method
        """
        surf = renpy.display.pgrender.surface((self.width, self.height), True)
        renpy.display.draw.mutated_surface(surf)
        self.blit(surf, (0, 0))
        canvas = renpy.display.render.Canvas(surf)
        return canvas

    def screen_rect(self, sx: float, sy: float, transform: list[list[int]]):
        return super().screen_rect(sx, sy, transform)

    def place(
        self,
        d,
        x=0,
        y=0,
        width=None,
        height=None,
        st=None,
        at=None,
        render=None,
        main=True,
    ):
        return super().place(d, x, y, width, height, st, at, render, main)

    def zoom(self, xzoom, yzoom):
        return super().zoom(xzoom, yzoom)

    def add_shader(self, shader):
        return super().add_shader(shader)

    def add_uniform(self, name, value):
        return super().add_uniform(name, value)

    def add_property(self, name, value):
        return super().add_property(name, value)

    # my methods

    @property
    def internal_render(self) -> renpy.Render:
        """if set will be used during blit() instead of using the parent class.
        This is used for conversions and is useful to prevent errors.
        and because if you use a r = renpy.render() and then self.blit(r) it will not work -> when you blit the self(render) into main render it will not work
        # TODO: instead of using this variable during the conversion, one could set all the variables to the old element in the new
        """
        return self._internal_render

    @internal_render.setter
    def internal_render(self, value: renpy.Render):
        self._internal_render = value

    @property
    def background_render(self) -> renpy.display.imagelike.Solid:
        """if set will be used as the background render when the parent render blit it.
        This is used for conversions and is useful to prevent errors.
        and because if you use a r = renpy.render() and then self.blit(r) it will not work -> when you blit the self(render) into main render it will not work
        # TODO: instead of using this variable during the conversion, one could set all the variables to the old element in the new
        """
        return self._background_render

    @background_render.setter
    def background_render(self, value: renpy.display.imagelike.Solid):
        self._background_render = value

    @property
    def renpygame_canvas(self) -> Canvas:
        if self._renpygame_canvas is None:
            if self.internal_render is None:
                self._renpygame_canvas = self.canvas()
            else:
                self._renpygame_canvas = self.internal_render.canvas()
        return self._renpygame_canvas

    @renpygame_canvas.setter
    def renpygame_canvas(self, value: Optional[Canvas]):
        self._renpygame_canvas = value

    def get_width(self) -> int:
        width, _ = self.get_size()
        return int(width)

    def get_height(self) -> int:
        _, height = self.get_size()
        return int(height)

    def import_renpy_render(self, renpy_render: renpy.Render):
        self = renpy_render
