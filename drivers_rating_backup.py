from sqlite3_helper import sqlite3_create, sqlite3_run
import os

sqlite3_file = 'drivers.sqlite3'
sqlite3_drivers_schema = 'drivers.sql'
sqlite3_trips_schema = 'trips.sql'

def run_query(query):
        sqlite3_output = sqlite3_run(sqlite3_file, query)

        return sqlite3_output

def sqlite3_check():
    schema_list=[sqlite3_drivers_schema, sqlite3_trips_schema]

    for schema in schema_list:
        if os.path.exists(schema) and os.path.isfile(schema):
            with open (schema) as file:
                sqlite3_create(sqlite3_file, file.read())
        else:
            output = f'Error: Required file "{schema}" is not exist'

            return output


def driver(driver_name, driver_family_name, driver_plate_number):
    if sqlite3_check() == None:
        if run_query(f'SELECT id FROM drivers WHERE name = "{driver_name}" AND family_name = "{driver_family_name}" AND plate_number = "{driver_plate_number}";') == []:
            
            add_record = f""" INSERT INTO drivers (name, family_name, plate_number) VALUES (
                            "{driver_name}", "{driver_family_name}", "{driver_plate_number}"
                            );"""
            run_query(add_record)
    else:
        output = sqlite3_check()
        return output

def trips(driver_name, driver_family_name, driver_plate_number):
    if sqlite3_check() == None:
        if run_query(f'SELECT id FROM drivers WHERE name = "{driver_name}" AND family_name = "{driver_family_name}" AND plate_number = "{driver_plate_number}";') == []:
            
            add_record = f""" INSERT INTO drivers (name, family_name, plate_number) VALUES (
                            "{driver_name}", "{driver_family_name}", "{driver_plate_number}"
                            );"""
            run_query(add_record)
    else:
        output = sqlite3_check()
        return output        

def main():

    driver_name = 'Amedd'
    driver_family_name = 'Hame'
    driver_plate_number = '125 ABC'
    
    driver(driver_name, driver_family_name, driver_plate_number)

if __name__ == "__main__":
    main()