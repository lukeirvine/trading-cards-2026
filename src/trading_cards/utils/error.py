class CsvReaderError(Exception):
    """Exception raised for errors in the CSVReader."""

    RED = "\033[31m"
    RESET = "\033[0m"

    def __init__(self, errors: list[str]):
        """
        :param errors: List of error messages to display.
        """
        message = "\n".join(errors)
        # Wrap the combined message in red color.
        super().__init__(f"{self.RED}{message}{self.RESET}")
