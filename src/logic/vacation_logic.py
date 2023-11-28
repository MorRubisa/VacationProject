from utils.dal import * 
from models.vacation_model import * 

#Users vacation logic:
class VacationLogic:

    # ctor - Create a DAL object:
    def __init__(self):
        self.dal = DAL()

    #Get all vacations:
    def get_all_vacations (self):
        sql = "SELECT * FROM vacations"
        result = self.dal.get_table(sql)
        vacations = VacationModel.dictionaries_to_vacations(result)
        return vacations

    # Add new vacation: ONLY admin CAN ADD 
    def add_vacation(self, vacation):
        sql = "INSERT INTO vacations (country_id, description, start_date, end_date, price, file_name) VALUES (%s, %s, %s, %s, %s, %s)"
        last_inserted_id = self.dal.insert(sql, (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price, vacation.file_name))
        return last_inserted_id
    
    # Update existing vacation: ONLY admin CAN UPDATE 
    def update_vacation(self, vacation):
        sql = "UPDATE vacations SET country_i= %s, description= %s, start_date=%s, end_date=%s, price=$ WHERE vacation_id = %s"
        row_count = self.dal.update (sql, (vacation.country_id, vacation.description, vacation.start_date, vacation.end_date, vacation.price))
        return row_count

    # Delete existing vacation: ONLY admin CAN DELETE
    def delete_vacation(self, vacation_id):
        sql = "DELETE FROM vacations WHERE vacation_id=%s"
        params = (vacation_id,)
        row_count = self.dal.delete(sql, params)
        return row_count
    
    # Close resources:
    def close(self):
        self.dal.close()

