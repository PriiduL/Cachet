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

    print("Did you enjoy the ride? (yes/no)")

    while True:
        user_input = input()
      
        if user_input == "no":
            do_you_like = 5
            print("Ouch, this is bad... So on a 1-10 scale, how would you rate the driving style of the driver?")
            while True:
                try:
                    condition_score = int(input())
                except ValueError:
                    print("Ouch, here is error, so try again")
                    continue
                if condition_score > 0 and condition_score < 11:
                    print("Mhm... On a 1-10 scale, how would you rate the condition of the car?")
                    while True:
                        try:
                            style_score = int(input())
                        except ValueError:
                            print("Ouch, here is error, so try again")
                            continue
                        if style_score > 0 and style_score < 11:
                            print("Okay, so on a 1-10 scale, how would you rate the behaviour of the driver?")
                            while True:
                                try:
                                    behaviour_score = int(input())
                                except ValueError:
                                    print("Ouch, here is error, so try again!")
                                    continue
                                if behaviour_score > 0 and behaviour_score < 11:
                                    print(do_you_like, condition_score, style_score, behaviour_score)
                                    exit()
                                else:
                                    print("The rating is in the wrong range, please try again!")
                        else:       
                            print("The rating is in the wrong range, please try again!")
                else:       
                    print("The rating is in the wrong range, please try again!")
  
        elif user_input == "yes":
            do_you_like = 10
            print("Nice! So on a 1-10 scale, how would you rate the driving style of the driver?")
            while True:
                try:
                    condition_score = int(input())
                except ValueError:
                    print("Ouch, here is error, so try again")
                    continue
                if condition_score > 0 and condition_score < 11:
                    print("Okaaay... On a 1-10 scale, how would you rate the condition of the car?")
                    while True:
                        try:
                            style_score = int(input())
                        except ValueError:
                            print("Ouch, here is error, so try again")
                            continue
                        if style_score > 0 and style_score < 11:
                            print("Cool, so on a 1-10 scale, how would you rate the behaviour of the driver?")
                            while True:
                                try:
                                    behaviour_score = int(input())
                                except ValueError:
                                    print("Ouch, here is error, so try again!")
                                    continue
                                if behaviour_score > 0 and behaviour_score < 11:
                                    print(do_you_like, condition_score, style_score, behaviour_score)
                                    exit()
                                else:
                                    print("The rating is in the wrong range, please try again!")
                        else:       
                            print("The rating is in the wrong range, please try again!")
                else:       
                    print("The rating is in the wrong range, please try again!")
        else:
            print("Try Again")
    # condition_score = input()
    # behaviour_score = input()
    # style_score = input()
    # driver_name = 'Amed'
    # driver_family_name = 'Hame'
    # driver_plate_number = '125 ABC'
    
    # driver(driver_name, driver_family_name, driver_plate_number)

if __name__ == "__main__":
    main()