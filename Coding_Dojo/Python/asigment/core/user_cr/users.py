from mysqlconnection import connectToMySQL

class users:
    def __init__(self, data) -> None:
        self.id=data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL('users').query_db(query)
        users = []
        for u in result:
            users.append(cls(u))
        return users
    
    @classmethod
    def add(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL('users').query_db(query,data)
        return result