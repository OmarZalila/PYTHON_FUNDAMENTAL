from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id=data["id"]
        self.name=data["name"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.ninjas=[]

    @classmethod
    def display(cls):
        query="SELECT * FROM dojos_and_ninjas.dojos"
        result=connectToMySQL('dojos_and_ninjas').query_db(query)
        All_dojos = []
        for dojo in result:
            All_dojos.append( cls(dojo) )
        return All_dojos
    
    @classmethod
    def add(cls,data):
        query="INSERT INTO dojos_and_ninjas.dojos (name) VALUES (%(name)s)"
        results=connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return results
    
    @classmethod
    def show(cls,data):
        query="""SELECT * FROM dojos_and_ninjas.dojos
                LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id
                WHERE dojos.id = %(id)s;"""
        result=connectToMySQL('dojos_and_ninjas').query_db(query,data)
        this_dojo=cls(result[0])
        all_ninjas=[]
        for ninja in result:
            all_ninjas.append(Ninja(ninja))
        this_dojo.ninjas=all_ninjas
        return this_dojo



