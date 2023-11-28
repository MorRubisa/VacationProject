#vacation MODEL:
class VacationModel:

    #Constructor -initial vacation data  
    def __init__ (self, id, country_id, description, start_date, end_date, price, file_name):
        self.id = id
        self.country_id = country_id
        self.description = description
        self.start_date =  start_date
        self.end_date=end_date
        self.price = price
        self.file_name = file_name

    #Display the vacation
    def display(self):
        print (f"ID:{self.id}, Country ID: {self.country_id}, Description: {self.description}, Start Date: {self.start_date}, End Date: {self.end_date}, Price: {self.price}")

    # Convert user Dictionary to vacation model
    @staticmethod
    def dictionary_to_vacation (dictionary):
        vacation = VacationModel(dictionary["id"], dictionary["country_id "], dictionary["description"], dictionary["start_date"], dictionary["end_date"], dictionary["price"], dictionary["file_name"])
        return vacation

    #Convert a list of vacations dictionaries to list of vacations models: 
    @staticmethod 
    def dictionaries_to_vacations (list_of_dictionaries):
        vacations_list = []
        for item in list_of_dictionaries: 
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations_list.append(vacation)
        return vacations_list
        




    
