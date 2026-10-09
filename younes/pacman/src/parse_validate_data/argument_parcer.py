from argparse import ArgumentParser
from pathlib import Path


class Parse_arguments:
    def __init__(self):
        self.Parser = ArgumentParser(
            "pacman",
            "pacman.py config.json",
            "pacman game"
            )
        self.Parser.add_argument("config")

    def run(self):
        args = self.Parser.parse_args()
        path = Path(args.config)
        return path