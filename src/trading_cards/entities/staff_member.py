import json

from trading_cards.utils.types import Department


class StaffMember:
    def __init__(
        self,
        image_path: str,
        name: str,
        position: str,
        years_worked: int,
        department: Department,
        bible_verse: str,
        question_1: str,
        answer_1: str,
        question_2: str,
        answer_2: str,
        question_3: str,
        answer_3: str,
        optional_front_file: str | None = None,
    ) -> None:
        self.image_path: str = image_path
        self.name: str = name
        self.position: str = position
        self.years_worked: int = years_worked
        self.department: Department = department
        self.questions: list[dict[str, str]] = [
            {"question": "Favorite Bible Verse", "answer": bible_verse},
            {"question": question_1, "answer": answer_1},
            {"question": question_2, "answer": answer_2},
            {"question": question_3, "answer": answer_3},
        ]
        self.optional_front_file: str | None = optional_front_file

    def print_data(self) -> None:
        data: dict[str, object] = {
            "image_path": self.image_path,
            "name": self.name,
            "position": self.position,
            "years_worked": str(self.years_worked),
            "department": self.department.value,
            "questions": self.questions,
        }
        print(json.dumps(data, indent=4))
