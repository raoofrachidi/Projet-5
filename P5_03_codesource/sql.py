"""Module that creates the database and tables
"""
import mysql.connector
from mysql.connector import errorcode
from category import Category
from product import Product
from favorite import Favorite
from database import my_cursor, connexion, upload_data
from constants import DATABASE_NAME, data_categories


tables = {}


# Definition of the function that creates the database
def create_database(cursor):
    """Function that creates the database and returns 1 if there is an error
    """
    try:
        cursor.execute(
            f"CREATE DATABASE {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f"Erreur dans la création de la base de données : {err}")
        exit(1)


def check_database():
    """Method checks if a database is created if not it creates it
    """
    try:
        my_cursor.execute(f"USE {DATABASE_NAME}")
        return False
    except mysql.connector.Error as err:
        print(f"La base de données {DATABASE_NAME} n'existe pas.")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(my_cursor)
            print(f"La base de données {DATABASE_NAME} a été créé avec succès.")
            connexion.database = DATABASE_NAME
            return True
        return False


# Function that creates the tables
def data_init():
    """Function that creates the different tables
    """
    # Create Category table (SQL REQUEST)
    categorie = Category()
    product = Product()
    favorite = Favorite()
    tables = {
        'Category': categorie.create(),
        'Product': product.create(),
        'Favorite': favorite.create()
    }
    # Create all tables of database
    for table_name in tables:
        table_description = tables[table_name]
        try:
            print(f"Création de la table {table_name} : ", end='')
            my_cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("existe déjà.")
            else:
                print(err.msg)
        else:

            print("OK")

    # Insert 7 categories in my category table(manually)
    categorie.insert_data()
    # The categories of my table
    category_index = list()
    for item in data_categories:
        category_index.append(item[1])

        # browse categories and insert data
    for index in enumerate(category_index):
        # Upload json file from api
        data_for_insert = upload_data(index[1], 1)
        # Insert data in Product table
        size = len(data_for_insert['products'])
        print(f'{index[1]} - produits: {size}')

        # The loop that inserts the data into my tables
        for i in range(size):
            try:
                store = data_for_insert['products'][i]['stores']
                name = data_for_insert['products'][i]['product_name']
                grade = data_for_insert['products'][i]['nutrition_grades_tags'][0]
                url = data_for_insert['products'][i]['url']
                id_category = index[0] + 1
            except(KeyError, TypeError):
                continue
            finally:
                product.insert_data(name, url, grade, id_category, store)
