from PIL import Image, ImageDraw


class ShapeBuilder:
    @staticmethod
    def add_rect_to_canvas(
        canvas: Image.Image,
        position: tuple[int, int] = (0, 0),
        size: tuple[int, int] = (100, 100),
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        draw = ImageDraw.Draw(canvas)
        draw.rectangle(
            (position[0], position[1], position[0] + size[0], position[1] + size[1]),
            fill=color,
        )

    @staticmethod
    def add_circle_to_canvas(
        canvas: Image.Image,
        position: tuple[int, int] = (0, 0),
        radius: int = 50,
        color: tuple[int, int, int] = (0, 0, 0),
    ) -> None:
        draw = ImageDraw.Draw(canvas)
        draw.ellipse(
            (
                position[0] - radius,
                position[1] - radius,
                position[0] + radius,
                position[1] + radius,
            ),
            fill=color,
        )
