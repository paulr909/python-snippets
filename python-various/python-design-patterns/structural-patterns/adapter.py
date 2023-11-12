from abc import ABC, abstractmethod


class PngInterface(ABC):
    @abstractmethod
    def draw(self):
        pass


class PngImage(PngInterface):
    def __init__(self, png):
        self.png = png
        self.format = "raster"

    def draw(self):
        print("drawing " + self.get_image())

    def get_image(self):
        return "png"


class SvgImage:
    def __init__(self, svg):
        self.svg = svg
        self.format = "vector"

    def get_image(self):
        return "svg"


class SvgAdapter(PngInterface):
    def __init__(self, svg):
        self.svg = svg

    def rasterize(self):
        return "rasterized " + self.svg.get_image()

    def draw(self):
        img = self.rasterize()
        print("drawing " + img)


# Class adapter


class ConvertingNonVector(Exception):
    # An exception used by class_adapter to check
    # whether an image can be rasterized
    pass


class ClassAdapter(PngImage, SvgImage):
    def __init__(self, image):
        self.image = image

    def rasterize(self):
        if self.image.format == "vector":
            return "rasterized " + self.image.get_image()
        else:
            raise ConvertingNonVector

    def draw(self):
        try:
            img = self.rasterize()
            print("drawing " + img)
        except ConvertingNonVector as e:
            print("drawing " + self.image.get_image())


if __name__ == "__main__":
    regular_png = PngImage("some data")
    regular_png.draw()

    example_svg = SvgImage("some data")
    example_adapter = SvgAdapter(example_svg)
    example_adapter.draw()

    # Use class adapter
    print("Class adapter called:")
    example_png = PngImage("some data")
    regular_png = ClassAdapter(example_png)
    regular_png.draw()

    example_svg = SvgImage("some data")
    example_adapter = ClassAdapter(example_svg)
    example_adapter.draw()
