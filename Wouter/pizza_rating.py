# Which are the top 10 pizza restaurants by rating?

import sqlite3

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
