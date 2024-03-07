from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import users

from flask import flash 

class Recipe:
    def __init__(self,data) :
        self.id=data["id"]
        self.name=data["name"]
        self.description=data["description"]
        self.instruction=data["instruction"]
        self.date_cooked=data["date_cooked"]
        self.under=data["under"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.user_id=data["user_id"]
    
    @classmethod
    def all_posted_recipe(cls):
        query="""
                SELECT * From recipes 
                JOIN users ON recipes.user_id = users.id;
                """
        result=connectToMySQL(DATABASE).query_db(query)
        all_recipes=[]
        for row in result:
            current_recipe = Recipe(row)
            user_data={
                **row,
                "id": row["users.id"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            current_recipe.posted_by=users.User(user_data)
            all_recipes.append(current_recipe)
        return all_recipes
    
    @classmethod
    def create(cls, data):
        
        query="""
                INSERT INTO recipes(name,description,instruction,date_cooked,under,user_id)
                VALUES (%(name)s,%(description)s,%(instruction)s,%(date_cooked)s,%(under)s,%(user_id)s);
            """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_one_recipe(cls,data):
        query=  """
                SELECT * FROM recipes 
                JOIN users ON users.id=recipes.user_id 
                WHERE recipes.id = %(id)s
                """
        result=connectToMySQL(DATABASE).query_db(query,data)
        one_recipe_user=cls(result[0])
        for row in result:
            data={
                **row,
                "id" : row["users.id"]
            }
            one_recipe_user.posted_by=users.User(data)
        return one_recipe_user
    @classmethod
    def get_id(cls,data):
        query="""
                SELECT * FROM recipes
                WHERE id = %(id)s;
                """
        result= connectToMySQL(DATABASE).query_db(query,data)

        display_recipe=cls(result[0])
        return display_recipe
    
    @classmethod
    def edit(cls,data):
        query="""
                UPDATE recipes
                SET name = %(name)s, description=%(description)s,instruction=%(instruction)s ,
                date_cooked=%(date_cooked)s,under=%(under)s
                WHERE id= %(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query="""
                DELETE FROM recipes 
                WHERE id=%(id)s
                """
        return connectToMySQL(DATABASE).query_db(query,data)


    
    @staticmethod
    def validate_recipe(data):    
        is_valid = True

        if(len(data["name"]) < 1):
            is_valid=False
            flash("*Name must not be blank ", "title")
        if(len(data["description"]) < 1):
            is_valid=False
            flash("*Description must not be blank ", "author")
        if(len(data["instruction"]) < 1):
            is_valid=False
            flash("*Instruction must not be blank ", "thought")
        if(data["date_cooked"]=="" ):
            is_valid=False
            flash("*Date must not be blank ", "date")
        return is_valid
        