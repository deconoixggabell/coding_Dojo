from My_sql_connection import connectToMySQL

class users:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.emial = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        @classmethod
        def get_all(cls):
            query = "SELECT * FROM users"
            results = connectToMySQL('users').query_db(query)
            users = []
            for u in results:
                users.append(cls(u))
            return users