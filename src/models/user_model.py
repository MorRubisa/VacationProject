#USER MODEL:for the use of any user: Admin or User
class UserModel:

    #Constructor -initial data members- User (Admin or User)
    def __init__ (self, user_id, first_name, last_name, email, password, role_id):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name =last_name
        self.email =  email
        self.password=password
        self.role_id = role_id

    #Display the user
    def display(self):
        print (f"ID:{self.user_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}, Password: {self.password}, Role: {self.role_id}")

    # Convert user Dictionary to user model
    @staticmethod
    def dictionary_to_user (dictionary):
        user= UserModel(dictionary["user_id"], dictionary["first_name"], dictionary["last_name"], dictionary["email"], dictionary["password"], dictionary["role_id"])
        return user

    #Convert a list of users dictionaries to list of users models: 
    @staticmethod 
    def dictionaries_to_users (list_of_dictionaries):
        users_list = []
        for item in list_of_dictionaries: 
            user = UserModel.dictionary_to_user(item)
            users_list.append(user)
        return users_list







