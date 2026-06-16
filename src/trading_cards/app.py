import os
from typing import List

from trading_cards.card.card_generator import CardGenerator, Side
from trading_cards.entities.staff_member import StaffMember
from trading_cards.utils.logger import Logger
from trading_cards.worker.csv_reader import CSVReader
from trading_cards.worker.exporter import Exporter, GeneratedImageMetadata


class App:
    def __init__(
        self,
        csv_file_path: str,
        image_dir: str,
        output_dir: str,
        generate_pdfs: bool = False,
        use_print_layout: bool = False,
        debug_mode: bool = False,
    ) -> None:
        self.csv_file_path: str = csv_file_path
        self.image_dir: str = image_dir
        self.output_dir: str = output_dir
        self.generate_pdfs: bool = generate_pdfs
        self.use_print_layout: bool = use_print_layout
        self.debug_mode: bool = debug_mode

    def run(self) -> None:
        reader = CSVReader(self.csv_file_path, self.image_dir)
        staff_members: list[StaffMember] = reader.read_csv()

        Logger.log_line()
        print("Generating cards...")
        Logger.log_line()

        generator = CardGenerator(self.output_dir, self.image_dir)
        generated_image_metadata: List[GeneratedImageMetadata] = []

        for staff_member in staff_members:
            front_image, back_image = generator.generate_card(staff_member)

            if self.use_print_layout:
                front_image = generator.add_print_layout(front_image, staff_member, Side.FRONT)
                back_image = generator.add_print_layout(back_image, staff_member, Side.BACK)

            front_file_name = f"{staff_member.name}_front.png"
            back_file_name = f"{staff_member.name}_back.png"
            save_dir = os.path.join(self.output_dir, staff_member.department.label)
            Exporter.save_canvas(
                canvas=front_image,
                file_name=front_file_name,
                save_dir=save_dir,
            )
            Exporter.save_canvas(
                canvas=back_image,
                file_name=back_file_name,
                save_dir=save_dir,
            )

            generated_image_metadata.append(
                {
                    "front_file_name": front_file_name,
                    "back_file_name": back_file_name,
                    "department": staff_member.department,
                    "years": staff_member.years_worked,
                }
            )
            print(f"Generated card for {staff_member.name}")

            Logger.log_line()

        if self.generate_pdfs:
            Exporter.save_pdf(
                card_data=generated_image_metadata,
                output_dir=self.output_dir,
                debug_mode=self.debug_mode,
            )
