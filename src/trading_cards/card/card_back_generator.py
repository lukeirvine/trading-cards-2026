import os
from typing import Tuple

from PIL import Image

from trading_cards.builder.image import ImageBuilder
from trading_cards.builder.text import TextBuilder
from trading_cards.entities.staff_member import StaffMember
from trading_cards.utils.constants import constants
from trading_cards.utils.types import ProseData, TextType


class CardBackGenerator:
    def __init__(self, staff_member: StaffMember) -> None:
        self.staff_member: StaffMember = staff_member
        size: Tuple[int, int] = (constants.CARD_WIDTH, constants.CARD_HEIGHT)
        self.canvas = Image.new("RGB", size, color=(255, 255, 255))

    def get_card_back(self) -> Image.Image:
        # Add design to back
        ImageBuilder.add_image_to_canvas(
            self.canvas,
            os.path.join(
                constants.MATERIAL_PATH,
                f"{self.staff_member.department.label}_back.png",
            ),
            (constants.CARD_WIDTH, constants.CARD_HEIGHT),
            (0, 0),
        )

        body_text: ProseData = []
        for question in self.staff_member.questions:
            body_text.append({"text": question["question"], "type": TextType.h3})
            body_text.append({"text": question["answer"], "type": TextType.body})

        body_start_pos = 180
        TextBuilder.add_body_to_canvas(
            text=body_text,
            canvas=self.canvas,
            position=(constants.BACK_MARGIN_HORIZONTAL, body_start_pos),
            max_width=constants.CARD_WIDTH - constants.BACK_MARGIN_HORIZONTAL * 2,
            max_height=constants.CARD_HEIGHT - constants.BACK_MARGIN_BOTTOM - body_start_pos,
            color=self.staff_member.department.text_color.value,
            body_indent=constants.BODY_INDENT,
        )

        return self.canvas
