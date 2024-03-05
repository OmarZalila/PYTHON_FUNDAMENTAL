from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
class Dojo:
    def __init__(self,data):
        self.name=data["name"]
        self.location=data["location"]
        self.language=data["language"]
        self.comment=data["comment"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
    
    @classmethod
    def save(cls,data):
        query="""
            INSERT INTO dojos(name,location,language,comment)
            VALUES(%(name)s,%(location)s,%(language)s,%(comment)s);
            """
        result=connectToMySQL('dojo_survey_schema').query_db(query,data)
        return result
    @classmethod
    def display(cls, data):
        query="""
                SELECT * FROM dojos
                WHERE id = %(id)s;
                """
        result=connectToMySQL('dojo_survey_schema').query_db(query, data)
        new_info=cls(result[0])
        return new_info

    @staticmethod
    def validate_dojo(data):
        is_valid = True # we assume this is true
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.","name")
            is_valid = False
        if len(data['location']) < 3:
            flash(" must choose a dojo location")
            is_valid = False
        if len(data['language']) < 2:
            flash("must choose a favorite language")
            is_valid = False
        if len(data['comment']) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid