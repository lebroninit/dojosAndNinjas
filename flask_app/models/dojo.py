from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_name(cls, id):
        query = f"SELECT name FROM dojos WHERE id={id}"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query)

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos ( name, created_at, updated_at) VALUES (%(name)s ,NOW(), NOW())"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    