from logic.user_logic import *

class UserFacade:

    def __init__(self):
        self.user = UserLogic()

    # Add new user:
    def add_user(self):
        user= UserModel(None, first_name= "Avi", last_name= "Ron", email= "blabla@gmail.com", password= "741", role_id="2")
        last_inserted_id = self.user_logic.add_user(user)
        user_id = last_inserted_id
        return user_id

    #close Resources:
    def close(self):
        self.user.close()

    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()

