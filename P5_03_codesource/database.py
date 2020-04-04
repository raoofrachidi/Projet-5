"""Module that tries to connect to the database and loads the
    data from the API into a JSON file
"""
import requests
import mysql.connector
from mysql.connector import errorcode
from constants import HOST, USER, PASSWORD, NUMBER_PRODUCT

# Creation a connexion to database
try:
    connexion = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Quelque chose ne va pas avec votre username ou votre password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de données n'existe pas")
    else:
        print(err)

my_cursor = connexion.cursor()

json_data = None


def upload_data(category, page):
    """Loads the API data into a Json file and returns it
    """
    api_search = 'https://world.openfoodfacts.org/cgi/search.pl?/get'
    payload = {
        'search_terms': '',
        'json': 1,
        'page_size': NUMBER_PRODUCT,
        'page': page,
        'categories': category
        }
    json_data = requests.get(api_search, params=payload).json()
    return json_data
