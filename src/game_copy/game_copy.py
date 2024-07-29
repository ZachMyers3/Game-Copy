from pathlib import Path
from shutil import copy
import zipfile


def extract_zip_to_dir(zip_file: Path, out_location: Path) -> None:
    """_summary_

    Args:
        zip_file (Path): _description_
        out_location (Path): _description_
    """
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(out_location)


def copy_to_dir(input_path: Path, output_path: Path) -> None:
    copy(input_path, output_path)


def find_file_in_folder(in_folder: Path) -> Path:
    p = in_folder.glob("**/*")
    files = [x for x in p if x.is_file()]
    if len(files) == 1:
        return files[0]
    else:
        return None


def game_copy(
    input_path: Path,
    output_path: Path,
    game_list: list[str],
):
    input_path = input_path.absolute()
    output_path = output_path.absolute()
    full_path_game_list: list[Path] = []
    for game in game_list:
        full_path_game_list.append(input_path / game)

    for game in full_path_game_list:
        if not game.exists():
            print(f"The game at path {game} does not exist")
            continue

        if not game.is_file():
            game = find_file_in_folder(in_folder=game)

        if game.suffix == ".zip":
            print(f"Unzipped {game} to {output_path}")
            extract_zip_to_dir(zip_file=game, out_location=output_path)
        else:
            print(f"Copying {game} to {output_path}")
            copy_to_dir(input_path=game, output_path=output_path)


if __name__ == "__main__":
    game_copy()
