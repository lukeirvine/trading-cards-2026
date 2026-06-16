class Constants:
    # Paths ========================
    MATERIAL_PATH: str = "materials"

    # Limits ========================
    MAX_YEARS: int = 14  # Maximum number of years worked at camp displayed on card (via stars)

    # Layouts ========================
    CARD_WIDTH: int = 750
    CARD_HEIGHT: int = 1050
    PRINT_WIDTH: int = 825
    PRINT_HEIGHT: int = 1125
    # Margins ========================
    FRONT_MARGIN_HORIZONTAL: int = 20
    BACK_MARGIN_HORIZONTAL: int = 40
    BACK_MARGIN_BOTTOM: int = 150
    BACK_MARGIN: int = 50
    BODY_INDENT: int = 20
    # Styles ========================
    HEADING_FONT: str = "fonts/Cleanow-j9v60.ttf"
    BODY_FONT: str = "fonts/BarlowSemiCondensed-Medium.ttf"
    # Misc ========================
    WRAP_HEURISTIC: float = 1.8  # Higher values allow longer lines before wrapping


constants: Constants = Constants()
