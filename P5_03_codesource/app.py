"""Module that groups the static methods of the main menu
"""
from product import Product
from favorite import Favorite
from functions import *
from constants import NUMBER_PRODUCT_PAGE, NUMBER_FAVORITE_PAGE, NUMBER_FAVORITE


class App:
    """
    Class that groups the different methods that process
    the data in the database
    """

    def __init__(self):
        self.user_choice = None
        self.response = None
        self.produit = Product()

    def display_favorite(self):
        """
        Function that displays favorites in the database
        """
        menu_favorite()
        self.user_choice = validate_entering(1, 2)
        favorite1 = Favorite()
        list_favorite = favorite1.get_all()
        if self.user_choice == 1:
            browse_favorite(NUMBER_FAVORITE, list_favorite)
        else:
            favorite1.empty_favorite()
            print('Tous les favoris ont été supprimés')
            os.system('pause')

    def display_product_category(self, index_category):
        """
        Function that displays the products of a category in the database
        """""
        list_product_categories = self.produit.get_product(index_category)
        browse_list(NUMBER_PRODUCT_PAGE, list_product_categories)
        self.user_choice = validate_entering(1, len(list_product_categories))
        print("-------------------------------------------------------")
        print(f"Vous avez choisi {list_product_categories[self.user_choice - 1][1][1]}\
            \nGrade: {list_product_categories[self.user_choice - 1][1][2]}")
        return list_product_categories[self.user_choice - 1]

    def display_best_product(self, grade, category):
        """Method that selects better quality products in relation to a product chosen by the user
        """""
        list_best_product_grade = self.produit.search_product(grade, category)
        browse_list(NUMBER_FAVORITE_PAGE, list_best_product_grade)
        return list_best_product_grade

    def save_product_substitute(self, product_choice, product_substitute, id_product_substitute, id_product):
        """
        Method saves selected product in favorite table in database
        """
        menu_save()
        self.response = yes_no()
        favorite = Favorite()
        if self.response == 'Oui':
            favorite.insert_data(
                product_choice,
                product_substitute,
                id_product_substitute,
                id_product
            )
            print("Produit enregistré aux Favoris")
        else:
            print("Ce produit n'est pas sauvegardé")
