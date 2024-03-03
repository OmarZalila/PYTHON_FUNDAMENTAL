
from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_schema.users;"
        results = connectToMySQL('users_schema').query_db(query)
        users_person = []
        for user in results:
            users_person.append( cls(user) )
        return users_person
    
    @classmethod
    def save(cls, data):
        query = """
                    INSERT INTO users_schema.users (first_name,last_name,email)
                    VALUES (%(first_name)s,%(last_name)s,%(email)s);
                """
        result = connectToMySQL('users_schema').query_db(query,data)
        print("the id of the created user is :" , result)
        return result

    @classmethod
    def get_one_by_id(cls,data):
        query= """
                SELECT * FROM users_schema.users WHERE id=%(id)s
                """
        results=connectToMySQL('users_schema').query_db(query , data)
        return cls(results[0])
    
    @classmethod
    def update(cls,data):
        query= """
                UPDATE users 
                SET first_name=%(first_name)s,
                    last_name=%(last_name)s,
                    email=%(email)s 
                    WHERE id = %(id)s;
                """
        return connectToMySQL('users_schema').query_db(query , data)
    @classmethod
    def delete_user(cls,data):
        query="DELETE FROM users_schema.users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

            
