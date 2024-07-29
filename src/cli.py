import typer

from pathlib import Path

from game_copy import game_copy

app = typer.Typer()


@app.command()
def command(
    input_path: Path = typer.Option(
        None, help="The path where files will be copied from"
    ),
    output_path: Path = typer.Option(
        None, help="The directory files will be copied into"
    ),
    game_list: Path = typer.Option(
        None, help="The list of file names to be copied from input to output"
    ),
) -> None:
    if input_path is None:
        raise FileNotFoundError("Input path is required")

    if output_path is None:
        raise FileNotFoundError("Output path is required")

    if game_list is None:
        raise FileNotFoundError("Game list is required")

    game_lines = []
    with open(game_list, "r") as _f:
        for line in _f:
            game_lines.append(line.strip())

    game_copy(
        input_path=input_path, output_path=output_path, game_list=game_lines
    )


def main():
    app()


if __name__ == "__main__":
    main()
