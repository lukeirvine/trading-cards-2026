import os
from typing import Tuple

from PIL import Image

from trading_cards.builder.image import ImageBuilder
from trading_cards.builder.text import TextBuilder
from trading_cards.entities.staff_member import StaffMember
from trading_cards.utils.constants import constants
from trading_cards.utils.types import TextType


class CardFrontGenerator:
    def __init__(self, staff_member: StaffMember, image_dir: str) -> None:
        self.staff_member: StaffMember = staff_member
        self.image_dir: str = image_dir
        size: Tuple[int, int] = (constants.CARD_WIDTH, constants.CARD_HEIGHT)
        self.canvas = Image.new("RGB", size, color=(255, 255, 255))

    def get_card_face(self) -> Image.Image:
        # Add main image to card
        ImageBuilder.add_image_to_canvas(
            self.canvas,
            os.path.join(self.image_dir, self.staff_member.image_path),
            (constants.CARD_WIDTH, constants.CARD_HEIGHT),
            (0, 0),
        )

        # Add border to card
        border_file_name = (
            self.staff_member.optional_front_file or f"{self.staff_member.department.label}_front.png"
        )
        ImageBuilder.add_mask_to_canvas(
            self.canvas,
            os.path.join(
                constants.MATERIAL_PATH,
                border_file_name,
            ),
            (constants.CARD_WIDTH, constants.CARD_HEIGHT),
            (0, 0),
        )

        # Add position to card.
        TextBuilder.add_text_to_canvas(
            text=self.staff_member.position,
            canvas=self.canvas,
            type=TextType.h2,
            position=(constants.FRONT_MARGIN_HORIZONTAL, 885),
            max_width=425,
            max_lines=1,
            vertical_align="center",
        )

        # Add name to card.
        TextBuilder.add_text_to_canvas(
            text=self.staff_member.name,
            canvas=self.canvas,
            type=TextType.h1,
            position=(constants.FRONT_MARGIN_HORIZONTAL, 950),
            max_width=675,
            max_lines=1,
            vertical_align="center",
            color=self.staff_member.department.text_color.value,
        )

        # Stars
        star_count = self.staff_member.years_worked
        if star_count > 13:
            star_count = 13
        for i in range(0, star_count):
            star_size = 55
            increment = star_size - 3
            ImageBuilder.add_mask_to_canvas(
                canvas=self.canvas,
                mask_path=os.path.join(constants.MATERIAL_PATH, "star.png"),
                size=(star_size, star_size),
                position=(11, 150 + i * increment),
                fill=self.staff_member.department.text_color.value,
            )

        return self.canvas
