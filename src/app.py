from logic.user_logic import * 
from logic.vacation_logic import *

#Need to change app.py to test.py

user_logic = UserLogic()
vacation_logic = VacationLogic()

# #Get all vacations
# result = vacation_logic.get_all_vacations()
# print (result)


# get user by sending email + password 
result = user_logic.get_one_user ("mor.rubisa@gmail.com", "nyb2017" )
result.display()



