import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

class Recipe:
    def __init__(self, data:dict) -> None:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.date_made = data['date_made']
        if 'first_name' in data:
            self.user = data['first_name']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data:dict) -> int:
        query = "INSERT INTO recipes (name,description,instructions, under_30, user_id, date_made) VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30)s, %(user_id)s, %(date_made)s);"
        result = connectToMySQL("recipes").query_db(query,data)
        return result

    @classmethod
    def get_all(cls) -> list:
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipes").query_db(query)
        recipes = []
        for u in results:
            recipes.append( cls(u) )
        return recipes

    @classmethod
    def get_all_with_users(cls) -> list:
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL("recipes").query_db(query)
        pprint(results)
        recipes = []
        for u in results:
            recipes.append( cls(u) )

        return recipes
    
    @classmethod
    def get_one(cls,data:dict) -> object:
        query  = "SELECT * FROM recipes WHERE id = %(id)s;"
        result = connectToMySQL("recipes").query_db(query,data)
        print(result)
        return cls(result[0])

    @classmethod
    def update(cls,data:dict) -> int:
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,under_30=%(under_30)s ,date_made=%(date_made)s WHERE id = %(id)s;"
        return connectToMySQL("recipes").query_db(query,data)

    @classmethod
    def destroy(cls,data:dict):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL("recipes").query_db(query,data)