""" Script to launch the program
"""
from sql import check_database, data_init
from functions import validate_entering, menu_main, exit_menu
from choice import ChoiceMenu


def main():
    """ Main function to start a script
    """
    # Initialisation data (upload json file from api)
    if check_database():
        data_init()

    # Main loop
    while True:
        menu_main()
        switcher = {
            1: ChoiceMenu.favorite_poster,
            2: ChoiceMenu.product_poster,
            3: ChoiceMenu.update_data,
            4: ChoiceMenu.leave
            }
        index = validate_entering(1, 4)
        switcher[index]()
        if index == 4:
            break
    exit_menu()


if __name__ == "__main__":
    main()
