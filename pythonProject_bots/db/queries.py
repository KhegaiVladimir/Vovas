class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone_number TEXT,
            last_appearence INTEGER,
            food_quality TEXT,
            clearity TEXT,
            additional_info TEXT
        )
    """

    CREATE_FOOD_TYPES_TABLE = '''
        CREATE TABLE IF NOT EXISTS type_of_food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    '''

    CREATE_FOOD_TABLE = '''
        CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            type_id INTEGER,
            FOREIGN KEY (type_id) REFERENCES type_of_food(id)
        )
    '''

    POPULATE_FOOD_TYPES = '''
        INSERT INTO type_of_food (name) VALUES ('блюда'), ('напитки'), ('салаты')
    '''

    POPULATE_FOOD = '''
        INSERT INTO food (name, price, type_id) VALUES ('Шашлык', 900, 1),
        ('Цезарь', 1500, 3),
        ('Кока-Кола', 160, 2)
    '''

    DROP_FOOD_TYPES_TABLE = "DROP TABLE IF EXISTS type_of_food"
    DROP_FOOD_TABLE = "DROP TABLE IF EXISTS food"
