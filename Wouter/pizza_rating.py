# Which are the top 10 pizza restaurants by rating?
# Deliveroo

import sqlite3


def deliveroo():
    connexion = sqlite3.connect("Databases/deliveroo.db")
    cursor = connexion.cursor()

    for row in cursor.execute("""

        SELECT
            restaurants.name, restaurants.rating
        FROM
            restaurants
            JOIN categories on restaurants.id = categories.restaurant_id
        WHERE
            categories.name = "Pizza"
        ORDER BY
            restaurants.rating DESC
        LIMIT 10;
    """):
        print(row[0], row[1])

# UberEats
def uber_eats():
    connexion = sqlite3.connect("Databases/ubereats.db")
    cursor = connexion.cursor()

    for row in cursor.execute("""

        SELECT
            restaurants.title, restaurants.rating__rating_value
        FROM
            restaurants
            JOIN restaurant_to_categories on restaurants.id = restaurant_to_categories.restaurant_id
        WHERE
            restaurant_to_categories.category = "Pizza"
        ORDER BY
            restaurants.rating__rating_value DESC
        LIMIT 10;
    """):
        print(row[0], row[1])

# UberEats
def takeaway():
    connexion = sqlite3.connect("Databases/takeaway.db")
    cursor = connexion.cursor()

    for row in cursor.execute("""
        SELECT
            restaurants.name, restaurants.ratings
        FROM
            restaurants
            JOIN categories_restaurants on restaurants.primarySlug = categories_restaurants.restaurant_id
        WHERE
            categories_restaurants.category_id = "italian-pizza_271"
        ORDER BY
            restaurants.ratings DESC
        LIMIT 10;
    """):
        print(row[0], row[1])

print('Deliveroo: ')
deliveroo()
print('Uber Eats: ')
uber_eats()
print('Takeaway: ')
takeaway()
