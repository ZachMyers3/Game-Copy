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


def copy_to_dir(
    input_path: Path, output_path: Path, rename_name: str | None
) -> None:
    copy(input_path, output_path)
    if rename_name is not None:
        current_file_name = input_path.name
        current_file_suffix = input_path.suffix
        output_file_name = output_path / current_file_name
        renamed_file_name = output_path / f"{rename_name}{current_file_suffix}"
        print(
            f"Subfolder was found, renaming {output_file_name} to {renamed_file_name} to remove subfolder"
        )
        output_file_name.rename(renamed_file_name)


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
            game_name = game.name
            game = find_file_in_folder(in_folder=game)
        else:
            game_name = None

        if game.suffix == ".zip":
            print(f"Unzipped {game} to {output_path}")
            extract_zip_to_dir(zip_file=game, out_location=output_path)
        else:
            print(f"Copying {game} to {output_path}")
            copy_to_dir(
                input_path=game, output_path=output_path, rename_name=game_name
            )


if __name__ == "__main__":
    game_copy()
