#python application 
import sqlite3

class ChocolateHouseDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def add_flavor(self, name, description, seasonal):
        self.cursor.execute("INSERT INTO flavors (name, description, seasonal) VALUES (?, ?, ?)", (name, description, seasonal))
        self.conn.commit()

    def add_ingredient(self, name, quantity):
        self.cursor.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
        self.conn.commit()

    def add_flavor_ingredient(self, flavor_id, ingredient_id):
        self.cursor.execute("INSERT INTO flavor_ingredients (flavor_id, ingredient_id) VALUES (?, ?)", (flavor_id, ingredient_id))
        self.conn.commit()

    def add_customer(self, name, email):
        self.cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        self.conn.commit()

    def add_suggestion(self, customer_id, flavor_name, description):
        self.cursor.execute("INSERT INTO suggestions (customer_id, flavor_name, description) VALUES (?, ?, ?)", (customer_id, flavor_name, description))
        self.conn.commit()

    def add_allergy(self, customer_id, ingredient_id):
        self.cursor.execute("INSERT INTO allergies (customer_id, ingredient_id) VALUES (?, ?)", (customer_id, ingredient_id))
        self.conn.commit()

    def get_flavors(self):
        self.cursor.execute("SELECT * FROM flavors")
        return self.cursor.fetchall()

    def get_ingredients(self):
        self.cursor.execute("SELECT * FROM ingredients")
        return self.cursor.fetchall()

    def get_customer_suggestions(self, customer_id):
        self.cursor.execute("SELECT * FROM suggestions WHERE customer_id = ?", (customer_id,))
        return self.cursor.fetchall()

    def get_customer_allergies(self, customer_id):
        self.cursor.execute("SELECT * FROM allergies WHERE customer_id = ?", (customer_id,))
        return self.cursor.fetchall()

# Example usage:
db = ChocolateHouseDB("chocolate_house.db")

# Add flavors
db.add_flavor("Strawberry Spring", "Sweet strawberry flavor", "Spring")
db.add_flavor("Minty Fresh", "Cool mint flavor", "Summer")

# Add ingredients
db.add_ingredient("Strawberries", 100)
db.add_ingredient("Mint Leaves", 50)

# Add flavor ingredients
db.add_flavor_ingredient(1, 1)
db.add_flavor_ingredient(2, 2)

# Add customers
db.add_customer("John Doe", "johndoe@example.com")
db.add_customer("Jane Doe", "janedoe@example.com")

# Add suggestions
db.add_suggestion(1, "Chocolate Orange", "A chocolate orange flavor would be great!")
db.add_suggestion(2, "Vanilla Swirl", "A vanilla swirl flavor sounds delicious!")

# Add allergies
db.add_allergy(1, 1)
db.add_allergy(2, 2)

# Get flavors
flavors = db.get_flavors()
print("Flavors:")
for flavor in flavors:
    print(flavor)

# Get ingredients
ingredients = db.get_ingredients()
print("\nIngredients:")
for ingredient in ingredients:
    print(ingredient)

# Get customer suggestions
suggestions = db.get_customer_suggestions(1)
print("\nCustomer Suggestions:")
for suggestion in suggestions:
    print(suggestion)

# Get customer allergies
allergies = db.get_customer_allergies(1)
print("\nCustomer Allergies:")
for allergy in allergies:
    print(allergy)