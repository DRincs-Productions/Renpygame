from typing import Optional
import renpy.exports as renpy

import pythonpackages.renpygame_pygame as pygame
from pythonpackages.renpygame.display import Surface
from pythonpackages.renpygame_pygame.image import *


# class Image(renpy.display.image.DynamicImage):
class Image(renpy.display.im.Image):
    """renpy: https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L709"""

    def __init__(
        self,
        filename: str,
        **properties,
    ):
        super().__init__(filename, **properties)
        self.rotate = 0

    def get_hash(self):
        return super().get_hash()

    def get_oversample(self):
        return super().get_oversample()

    def load(self, unscaled=False):
        return super().load(unscaled)

    def predict_files(self) -> list[str]:
        return super().predict_files()

    # my methods

    @property
    def size(self) -> tuple[int, int]:
        return self.pygame_image.get_size()

    @property
    def width(self) -> int:
        width, _ = self.size
        return width

    @property
    def height(self) -> int:
        _, height = self.size
        return height

    @property
    def imagename(self) -> str:
        images_names = self.predict_files()
        if len(images_names) > 0:
            return images_names[0]
        else:
            raise FileNotFoundError(
                f"renpygame.image.Image.imagename: Image not found: {self}"
            )

    @property
    def file(self):
        path = "images/" + self.imagename
        return renpy.open_file(path)

    @property
    def pygame_image(self) -> pygame.Surface:
        image = pygame.image.load(self.file)  # type: ignore
        image = image.convert()
        return image

    def convert(self, st: float, at: float) -> Surface:
        # TODO: try use renpy.load_surface
        surface = Surface(self.size)
        transform = self.transform
        if transform:
            render = renpy.render(transform, self.width, self.height, st, at)
        else:
            render = renpy.render(self, self.width, self.height, st, at)
        surface.blit(render, (0, 0))
        # TODO: try use olther methods
        surface.internal_render = render
        return surface

    @property
    def transform(self) -> Optional[renpy.display.transform.Transform]:
        """https://github.com/renpy/renpy/blob/master/renpy/display/transform.py#L505"""
        # TODO: to improve
        if self.rotate and self.rotate != 0:
            return renpy.display.transform.Transform(self.imagename, rotate=self.rotate)
        return None

    @property
    def rotate(self) -> Optional[int]:
        return self._rotation

    @rotate.setter
    def rotate(self, value: int):
        self._rotation = value


class Flip(renpy.display.im.Flip):
    """renpy: https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L1064"""

    def __init__(
        self,
        im: Image,
        horizontal=False,
        vertical=False,
        **properties,
    ):
        super().__init__(im, horizontal, vertical, **properties)

    def get_hash(self):
        return super().get_hash()

    def load(self):
        return super().load()

    def predict_files(self) -> list[str]:
        return super().predict_files()

    # my methods

    @property
    def size(self) -> tuple[int, int]:
        return self.pygame_image.get_size()

    @property
    def width(self) -> int:
        width, _ = self.size
        return width

    @property
    def height(self) -> int:
        _, height = self.size
        return height

    @property
    def imagename(self) -> str:
        images_names = self.predict_files()
        if len(images_names) > 0:
            return images_names[0]
        else:
            raise FileNotFoundError(
                f"renpygame.image.Flip.imagename: Image not found: {self}"
            )

    @property
    def file(self):
        path = "images/" + self.imagename
        return renpy.open_file(path)

    @property
    def pygame_image(self) -> pygame.Surface:
        image = pygame.image.load(self.file)  # type: ignore
        image = image.convert()
        return image

    def convert(self, st: float, at: float) -> Surface:
        return Image.convert(self, st, at)


class Scale(renpy.display.im.Scale):
    """https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L947"""

    def __init__(self, im, width, height, bilinear=True, **properties):
        super().__init__(im, width, height, bilinear, **properties)

    def get_hash(self):
        return super().get_hash()

    def load(self):
        return super().load()

    def predict_files(self) -> list[str]:
        return super().predict_files()

    # my methods

    @property
    def size(self) -> tuple[int, int]:
        return self.pygame_image.get_size()

    @property
    def width(self) -> int:
        width, _ = self.size
        return width

    @property
    def height(self) -> int:
        _, height = self.size
        return height

    @property
    def imagename(self) -> str:
        images_names = self.predict_files()
        if len(images_names) > 0:
            return images_names[0]
        else:
            raise FileNotFoundError(
                f"renpygame.image.Scale.imagename: Image not found: {self}"
            )

    @property
    def file(self):
        path = "images/" + self.imagename
        return renpy.open_file(path)

    @property
    def pygame_image(self) -> pygame.Surface:
        image = pygame.image.load(self.file)  # type: ignore
        image = image.convert()
        return image

    def convert(self, st: float, at: float) -> Surface:
        return Image.convert(self, st, at)


class Rotozoom(renpy.display.im.Rotozoom):
    """https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L1113"""

    def __init__(self, im, angle, zoom, **properties):
        super().__init__(im, angle, zoom, **properties)

    def get_hash(self):
        return super().get_hash()

    def load(self):
        return super().load()

    def predict_files(self) -> list[str]:
        return super().predict_files()

    # my methods

    @property
    def size(self) -> tuple[int, int]:
        return self.pygame_image.get_size()

    @property
    def width(self) -> int:
        width, _ = self.size
        return width

    @property
    def height(self) -> int:
        _, height = self.size
        return height

    @property
    def imagename(self) -> str:
        images_names = self.predict_files()
        if len(images_names) > 0:
            return images_names[0]
        else:
            raise FileNotFoundError(
                f"renpygame.image.Rotozoom.imagename: Image not found: {self}"
            )

    @property
    def file(self):
        path = "images/" + self.imagename
        return renpy.open_file(path)

    @property
    def pygame_image(self) -> pygame.Surface:
        image = pygame.image.load(self.file)  # type: ignore
        image = image.convert()
        return image

    def convert(self, st: float, at: float) -> Surface:
        return Image.convert(self, st, at)


def load(path: str) -> Image:
    """https://www.pygame.org/docs/ref/image.html#pygame.image.load"""
    return Image(path)


# MatrixColor


class MatrixColor(renpy.display.im.ImageBase):
    """https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L1400"""

    def __init__(self, im, matrix, **properties):
        super().__init__(im, matrix, **properties)

    def get_hash(self):
        return super().get_hash()

    def load(self):
        return super().load()

    def predict_files(self) -> list[str]:
        return super().predict_files()

    # my methods

    @property
    def size(self) -> tuple[int, int]:
        return self.pygame_image.get_size()

    @property
    def width(self) -> int:
        width, _ = self.size
        return width

    @property
    def height(self) -> int:
        _, height = self.size
        return height

    @property
    def imagename(self) -> str:
        images_names = self.predict_files()
        if len(images_names) > 0:
            return images_names[0]
        else:
            raise FileNotFoundError(
                f"renpygame.image.MatrixColor.imagename: Image not found: {self}"
            )

    @property
    def file(self):
        path = "images/" + self.imagename
        return renpy.open_file(path)

    @property
    def pygame_image(self) -> pygame.Surface:
        image = pygame.image.load(self.file)  # type: ignore
        image = image.convert()
        return image

    def convert(self, st: float, at: float) -> Surface:
        return Image.convert(self, st, at)


def Grayscale(im, desat=(0.2126, 0.7152, 0.0722), **properties):
    """https://github.com/renpy/renpy/blob/master/renpy/display/im.py#L1792"""
    return MatrixColor(im, matrix.saturation(0.0, desat), **properties)
