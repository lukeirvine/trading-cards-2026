import sys

from trading_cards.app import App


def main() -> None:
    debug_mode = "--from-watcher" in sys.argv
    app = App(
        csv_file_path="input/staff-test-one.csv",
        image_dir="images",
        output_dir="output",
        generate_pdfs=True,
        use_print_layout=True,
        debug_mode=debug_mode,
    )
    app.run()


if __name__ == "__main__":
    main()
