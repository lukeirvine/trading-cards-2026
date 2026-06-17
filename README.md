# Trading Cards Generator 2026

A Python-based system for generating custom trading cards with staff information from a csv file. The intent is to accumulate a library of helpful methods for adding text and images to a Pillow canvas, so minimal work is needed to design trading cards in future years.

<p align="center">
  <img src="./demo_front.png" alt="Sample trading card front" width="45%" />
  <img src="./demo_back.png" alt="Sample trading card back" width="45%" />
</p>

## Features

- Generate trading cards from staff data in CSV format
- Custom styling for different departments
- Automatic image processing and resizing
- Automatic text scaling and resizing based on available space
- PDF compilation
- Turn on/off print bleed margins
- Can handle card rarity in the print PDF based on tenure

## Prerequisites

- Python 3.8 or higher
- Poetry (>=1.2.0) installed globally
- Homebrew (for macOS users)

### Install Poetry

Poetry is required to manage dependencies and virtual environments. Install it globally using one of the following:

```bash
# macOS (Homebrew)
brew install poetry

# All platforms
curl -sSL https://install.python-poetry.org | python3 -
```

## Installation

1. Clone the repository:

```bash
git clone [repository-url]
cd trading-cards-2026
```

2. Install Python dependencies (Poetry will create a `.venv` in the project root automatically):

```bash
poetry install --with dev
```

## Project Structure

```
TRADING-CARDS-2026/
├── .vscode/
│   └── settings.json
├── fonts/ # font files referenced in src/trading_cards/utils/constants
├── images/ # for images of staff members
├── input/ # for your csv files
├── materials/ # contains design image files
├── output/ # for output files
├── src/
│   └── trading_cards/
│       ├── app.py
│       ├── main.py
│       ├── builder/ # methods for manipulating Pillow canvases
│       │   ├── image.py
│       │   ├── shape.py
│       │   └── text.py
│       ├── card/
│       │   ├── card_generator.py # glues together front/back generators
│       │   ├── card_front_generator.py # edit to fit design
│       │   └── card_back_generator.py # edit to fit design
│       ├── entities/
│       │   └── staff_member.py # handles information from csv
│       ├── utils/
│       │   ├── constants.py
│       │   ├── error.py
│       │   ├── helpers.py
│       │   ├── logger.py # helpful for logging in color
│       │   └── types.py
│       └── worker/
│           ├── csv_reader.py # parses and verifies csv file
│           └── exporter.py
```

## Usage

1. Prepare your staff data in CSV format with the following columns:
   - `image_path`
     - The file name of the image of the staff member.
   - `name`
   - `position`
   - `years_worked`
   - `department`
     - This should be an enum key of `Department` in [`types.py`](src/trading_cards/utils/types.py)
   - `bible_verse`
   - `question_1`
   - `answer_1`
   - `question_2`
   - `answer_2`
   - `question_3`
   - `answer_3`
   - `optional_front_file`
     - This is for if a staff member needs an exclusive border asset for
       the front of the card.

2. Place your csv in the `input` directory and provide the path to it in [`main.py`](src/trading_cards/main.py)
3. Place staff images in the `images/` directory

4. Run the application:

```bash
poetry run python src/trading_cards/main.py
```

5. Run in watch mode:

```bash
poetry run python watcher.py
```

## Contributing

A pre-commit script is configured to run on each commit and will only permit commits if formatting and typing are correct and testing runs successfully.

Often, a commit will fail, but black and/or isort will make necessary changes for you, and you can create a successful commit by simply running the commit command again.

## For 2027 Trading Cards:

1. Create a new repo for 2027
2. Clone this repo, copy the code to a new dir, link up with the new 2027 repo.
3. Edit the files in `src/trading_cards/card`, taking advantage of the methods in
   `src/trading_cards/builder` and `src/trading_cards/utils`.

## Acknowledgments

- Card design by Kate Byrd
