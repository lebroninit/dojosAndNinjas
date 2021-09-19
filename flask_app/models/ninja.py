from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojos_id = data['dojos_id']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_all_from(cls, id):
        query = f"SELECT * FROM ninjas WHERE id = {id};"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas ( first_name , last_name , age, created_at, updated_at, dojos_id) VALUES ( %(fName)s , %(lName)s , %(age)s , NOW() , NOW() , %(dojoid)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )

