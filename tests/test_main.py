from typing import Any

from trading_cards.main import main


def test_main_prints_hello(capsys: Any) -> None:
    # Call the function
    main()
    # Capture stdout
    captured = capsys.readouterr()
    # Assert it printed what we expect
    assert "Hello, world!" in captured.out
