class Constants:
    # Paths ========================
    MATERIAL_PATH: str = "materials"

    # Limits ========================
    MAX_YEARS: int = 14  # Maximum number of years worked at camp displayed on card (via stars)

    # Layouts ========================
    # All dimensions are in pixels and assume a 300 DPI resolution for printing. The card design itself
    # is 750x1050, but the print layout adds a border around it, making the total dimensions 825x1125.
    # This allows for a 0.25 inch border on all sides when printed at 300 DPI. The margins are designed
    # to ensure that text and other elements are not too close to the edges of the card, especially when
    # printed with the border.
    CARD_WIDTH: int = 750  # The width of the card design (not including print layout)
    CARD_HEIGHT: int = 1050  # The height of the card design (not including print layout)
    PRINT_WIDTH: int = 825  # The width of the card design including print layout
    PRINT_HEIGHT: int = 1125  # The height of the card design including print layout
    # Margins ========================
    FRONT_MARGIN_HORIZONTAL: int = 20
    BACK_MARGIN_HORIZONTAL: int = 80
    BACK_MARGIN_BOTTOM: int = 150
    BACK_MARGIN: int = 50
    BODY_INDENT: int = 20
    # Styles ========================
    HEADING_FONT: str = "fonts/CabinSketch-Bold.ttf"
    SUBHEADING_FONT: str = "fonts/Quicksand-VariableFont_wght.ttf"
    H3_FONT: str = "fonts/CabinSketch-Regular.ttf"
    BODY_FONT: str = "fonts/Quicksand-VariableFont_wght.ttf"
    # Misc ========================
    WRAP_HEURISTIC: float = 1.8  # Higher values allow longer lines before wrapping


constants: Constants = Constants()
