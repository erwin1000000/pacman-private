from src.parse_validate_data.argument_parcer import Parse_arguments
from src.parse_validate_data.json_filter_validation import (
    FilterValidateExtract
    )
from src.pacman.game import Game


def main():
    parcer = Parse_arguments()
    path = parcer.run()
    f_v_e = FilterValidateExtract(path)
    data = f_v_e.prossess()
    for d in data:
        print(d)
    game = Game(data)
    game.run()






if __name__ == "__main__":
    main()


