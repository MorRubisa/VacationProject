import mysql.connector  # pip install mysql-connector-python

# Data Access Layer - performs actions directly in the database:
class DAL:

    # Constructor (ctor) - create connection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="vacations")
            
    #Return a Table    
    def get_table(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            table = cursor.fetchall()
            return table

    #Return a scalar from the table (self) according to the SQL
    def get_scalar(self, sql, params=None):
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            scalar = cursor.fetchone()
            return scalar

    #Insert values (according to the SQL + params) to the table (self) 
    def insert(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            last_row_id = cursor.lastrowid
            return last_row_id

    #Update values (according to the SQL + params) to the table (self) 
    def update(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    #Delete from Table
    def delete(self, sql, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(sql, params)
            self.connection.commit() # Save to database now.
            row_count = cursor.rowcount
            return row_count

    # Close connection:
    def close(self):
        self.connection.close()
