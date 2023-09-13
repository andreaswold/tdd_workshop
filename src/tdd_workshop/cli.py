import click
from tdd_workshop.io import read_coordinates  # type: ignore
from tdd_workshop.treasure_hunt import find_first_treasure_candidate


@click.command()
@click.argument("file_name", type=click.Path(exists=True))
def main(file_name: str) -> None:
    coordinates = read_coordinates(file_name)
    treasure_index = find_first_treasure_candidate(coordinates, 1)
    treasure_location = coordinates[treasure_index]
    print(f"Found the treasure at: {treasure_location}")
