from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data) -> None:
        self.id=data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    @classmethod
    def add(cls, data):
        query = "INSERT INTO reg_login.users (first_name, last_name, email,password,created_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW());"
        result = connectToMySQL('reg_login').query_db(query,data)
        return result
    
    # def full_name(self):
    #     return f"{self.first_name}{self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('reg_login').query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users
    
    @classmethod
    def get_id(cls,data):
        query = "SELECT * FROM reg_login.users WHERE id = %(id)s;"
        result = connectToMySQL('reg_login').query_db(query,data)
        return cls(result[0])

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM reg_login.users WHERE email = %(email)s;"
        result = connectToMySQL('reg_login').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @staticmethod
    def validate_reg(user):
        is_valid = True
        query = "SELECT * FROM reg_login.users WHERE email = %(email)s;"
        result = connectToMySQL(User.reg_login).query_db(query,user)
        if len(result) > 1:
            flash("Email taken.")
            is_calide = False
        if not EMAIL_REGEX.match(user['email']):
            flash("email cann't be used")
            is_valid = False
        if len(user['first_name'] < 1):
            flash("First name must be more than one charactor")
            is_valid = False
        if len(user['last_name'] < 1):
            flash("Last name must be more than 1 charactor")
            is_valid = False
        if len(user['Password'] < 8):
            flash("password must be at leat 8 charactor")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Password do not match")
        return is_valid
    
    # @staticmethod
    # def val_login(user):
    #     is_valid = True
    #     query = "SELECT * FROM reg_login.users WHERE email = %(email)s;"
    #     result = connectToMySQL(User.reg_login).query_db(query,user)
    #     return is_valid



    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, password=NOW() WHERE id=%(id)s;"
    #     return connectToMySQL('users').query_db(query,data)
    
    # @classmethod
    # def delete(cls,data):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('users').query_db(query,data)