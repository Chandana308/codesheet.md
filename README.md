CREATE TABLE flavors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    seasonal TEXT CHECK(seasonal IN ('Spring', 'Summer', 'Fall', 'Winter'))
);

CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER
);

CREATE TABLE flavor_ingredients (
    flavor_id INTEGER,
    ingredient_id INTEGER,
    FOREIGN KEY(flavor_id) REFERENCES flavors(id),
    FOREIGN KEY(ingredient_id) REFERENCES ingredients(id)
);

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE suggestions (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    flavor_name TEXT,
    description TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);

CREATE TABLE allergies (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    ingredient_id INTEGER,
    FOREIGN KEY(customer_id) REFERENCES customers(id),
    FOREIGN KEY(ingredient_id) REFERENCES ingredients(id)
);
