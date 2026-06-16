import datetime
import os
from typing import List, TypedDict

from PIL import Image

from trading_cards.entities.staff_member import Department
from trading_cards.utils.logger import Logger, PrintColor


class GeneratedImageMetadata(TypedDict):
    front_file_name: str
    back_file_name: str
    department: Department
    years: int


class Exporter:
    @staticmethod
    def save_canvas(canvas: Image.Image, file_name: str, save_dir: str) -> None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        canvas.save(os.path.join(save_dir, file_name))

    @staticmethod
    def save_pdf(
        card_data: List[GeneratedImageMetadata],
        output_dir: str,
        debug_mode: bool = False,
    ) -> None:
        print("\nSaving PDF...")

        # Create the folder to save the image
        pdf_folder = f"{output_dir}/pdfs"
        if not os.path.exists(pdf_folder):
            os.makedirs(pdf_folder)

        timestamp = datetime.datetime.now().strftime("%Y:%m:%d %H-%M-%S") if not debug_mode else "debug"
        if not os.path.exists(os.path.join(pdf_folder, timestamp)):
            os.makedirs(os.path.join(pdf_folder, timestamp))
        pdf_folder = os.path.join(pdf_folder, timestamp)
        pdf_path = f"{pdf_folder}/mivoden-trading-cards-{timestamp}.pdf"
        pdf_rarity_path = f"{pdf_folder}/mivoden-trading-cards-rarity-{timestamp}.pdf"

        # add iamges
        images: list[Image.Image] = []
        rarity_images: list[Image.Image] = []
        for card in card_data:
            front_image = Image.open(f"{output_dir}/{card['department'].label}/{card['front_file_name']}")
            back_image = Image.open(f"{output_dir}/{card['department'].label}/{card['back_file_name']}")

            images.append(front_image)
            images.append(back_image)

            # set frequency
            frequency = 3
            years = card["years"]
            if years >= 3:
                frequency = 2
            if years >= 6:
                frequency = 1

            for _ in range(frequency):
                rarity_images.append(front_image)
                rarity_images.append(back_image)

        # save the pdfs
        images[0].save(pdf_path, "PDF", resolution=300.0, save_all=True, append_images=images[1:])
        Logger.log(f"PDF saved to {pdf_path}", PrintColor.GREEN)
        rarity_images[0].save(
            pdf_rarity_path,
            "PDF",
            resolution=300.0,
            save_all=True,
            append_images=rarity_images[1:],
        )
        Logger.log(f"Rarity PDF saved to {pdf_rarity_path}", PrintColor.GREEN)
