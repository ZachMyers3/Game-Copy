import typer

from pathlib import Path

from game_copy import game_copy

app = typer.Typer()


def print_results(input_path: Path, output_path: Path, game_list: list[str]):
    for game in game_list:
        print(f"Would copy {game} to {output_path}")


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
    exclude: list[str] = typer.Option(
        [],
        help="A string a file may contain to skip being copied, e.g. BETA, DEMO, etc.",
    ),
    dry_run: bool = typer.Option(
        False, help="If enabled just list all files to copy and exit"
    ),
) -> None:
    if input_path is None:
        raise FileNotFoundError("Input path is required")

    if output_path is None:
        raise FileNotFoundError("Output path is required")

    # pylance being weird with typer
    game_list_wtf = game_list

    game_lines = []
    if game_list_wtf is not None:
        with open(game_list, "r") as _f:
            for line in _f:
                game_lines.append(line.strip())
    else:
        print("No game list provided, gathering all files in folder")
        for file in input_path.iterdir():
            include: bool = True
            for exclusion in exclude:
                if exclusion in str(file):
                    print(
                        f"Excluding {file} because of exclusion string '{exclusion}'"
                    )
                    include = False
                    break
            if include:
                game_lines.append(file)

    print(f"{game_lines=}")

    if dry_run:
        print_results(
            input_path=input_path,
            output_path=output_path,
            game_list=game_lines,
        )
    else:
        game_copy(
            input_path=input_path,
            output_path=output_path,
            game_list=game_lines,
        )


def main():
    app()


if __name__ == "__main__":
    main()
