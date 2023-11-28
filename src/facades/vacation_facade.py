from logic.vacation_logic import *

class VacationFacade:


    def __init__(self):
        self.vacation = VacationLogic()


    # Add vacation:
    def add_vacation(self):
        vacation = VacationModel(None, 5, "Have Fun in Petah-Tikva", "2024-12-1", "2024-12-02", "20", "PT")
        last_inserted_id = self.vacation_logic.add_vacation (vacation)
        vacation.id= last_inserted_id


    # #Delete vacation:
    # def delete_vacation(self):
    
    # Close resources:
    def close(self):
        self.vacation.close()

    # Enabling "with" keyword usage:
    def __enter__(self):
        return self

    # Disposing when exiting "with" block:
    def __exit__(self, ex_type, ex_value, ex_trace):
        self.close()
