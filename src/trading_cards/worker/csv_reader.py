import csv
import os

from trading_cards.entities.staff_member import StaffMember
from trading_cards.utils.error import CsvReaderError
from trading_cards.utils.types import Department


class CSVReader:
    def __init__(self, file_path: str, image_dir: str) -> None:
        self.file_path: str = file_path
        self.image_dir: str = image_dir

    def read_csv(self) -> list[StaffMember]:
        staff_members: list[StaffMember] = []
        errors: list[str] = []

        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=2):
                dept_str: str = row["department"]
                if not Department.is_valid(dept_str):
                    errors.append(f"Invalid department '{dept_str}' on row {i}")
                    continue
                staff_member = StaffMember(
                    image_path=row["image_path"],
                    name=row["name"],
                    position=row["position"],
                    years_worked=int(row["years_worked"]),
                    department=Department.get_enum_by_label(dept_str),
                    bible_verse=row["bible_verse"],
                    question_1=row["question_1"],
                    answer_1=row["answer_1"],
                    question_2=row["question_2"],
                    answer_2=row["answer_2"],
                    question_3=row["question_3"],
                    answer_3=row["answer_3"],
                    optional_front_file=row.get("optional_front_file", None),
                )
                staff_members.append(staff_member)

        if errors:
            header = f"There were {len(errors)} department errors:"
            raise CsvReaderError([header] + errors)

        self._check_data(staff_members)
        return staff_members

    def _check_data(self, staff_members: list[StaffMember]) -> None:
        i = 0
        errors: list[str] = []
        for sm in staff_members:
            # check that the image exists
            if not os.path.exists(self.image_dir + "/" + sm.image_path):
                errors.append(
                    f'IMAGE ERROR {i + 2}: The image "{sm.image_path}" for {sm.name} '
                    f"doesn't exist. Check line {i + 2} in the csv file.",
                )

            # check that name is valid
            if "/" in sm.name:
                errors.append(f"The name column on row {i + 2} should not contain '/'")

            i += 1

        if len(errors) > 0:
            header = f"There were {len(errors)} errors with your data:"
            raise CsvReaderError([header] + errors)
