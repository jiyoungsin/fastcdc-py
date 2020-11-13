import click
from fastcdc import fastcdc
from hashlib import sha256
from os.path import dirname, join


@click.command()
@click.argument("file", type=click.File("rb"))
def split(file):
    root_path = dirname(file.name)

    result = fastcdc(file, fat=True, hf=sha256)
    for chunk in result:
        file_path = join(root_path, chunk.hash)
        with open(file_path, "wb") as outfile:
            outfile.write(chunk.data)
