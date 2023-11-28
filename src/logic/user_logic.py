from utils.dal import * 
from models.user_model import * 

#Users Business logic:
class UserLogic:
    
    # ctor - Create a DAL object:
    def __init__(self):
        self.dal = DAL()

    #Get one user:
    def get_one_user (self, email, password):
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"
        result = self.dal.get_scalar(sql, (email, password))
        if result is None: return None #if the email doesn't exist
        user = UserModel.dictionary_to_user(result)
        return user
    
    #Check if an EMAIL exist (exist = TRUE. NOT = FALSE)
    def is_email_exist (self, user_email):
        sql = "SELECT * FROM users WHERE email = %s"
        result = self.dal.get_scalar(sql, (user_email, ))
        if result is None:return False
        return True
    
    # Add new USER:
    def add_user(self, user):
        sql = "INSERT INTO users (first_name, last_name, email, password, role_id) VALUES (%s, %s, %s, %s, %s)"
        last_inserted_id = self.dal.insert(sql, (user.first_name, user.last_name, user.email, user.password, user.role_id))
        return last_inserted_id
    
    #ADD LIKE
    def get_like(self, user_id, vacation_id):
        sql = "INSERT INTO likes (user_id, vacation_id) VALUES (%s, %s)" 
        row_count = self.dal.insert(sql, (user_id, vacation_id))
        return row_count
    
    #Unlike = DELETE
    def get_unlike (self, id_user, id_vacation):
        sql = "DELETE FROM likes WHERE user_id = %s AND vacation_id=%s"
        row_count = self.dal.delete(sql, (id_user, id_vacation))
        return row_count

    # Close resources:
    def close(self):
        self.dal.close()
        