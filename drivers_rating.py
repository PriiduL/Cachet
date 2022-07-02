from sqlite3_helper import sqlite3_create, sqlite3_run
import os
import re
sqlite3_file = 'drivers.sqlite3'
sqlite3_drivers_schema = 'drivers.sql'
sqlite3_trips_schema = 'trips.sql'
sqlite3_file_trips = 'trips.sqlite3'
from statistics import mean


def remove_sym(name):
    name = re.sub(r"[\[\]]",'',name)
    name = name.strip("()")
    name = name.replace("'", "")
    name = name.replace(",", "")
    return name

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

def trips(do_you_like, condition_score, style_score, behaviour_score, driver_id, avg_trip_score):
    if sqlite3_check() == None:
        if run_query(f'SELECT id FROM trips WHERE driver_id = "{driver_id}" AND do_you_like = "{do_you_like}" AND style = "{style_score}" AND condition = "{condition_score}" AND behaviour = "{behaviour_score}" AND avg_trip_score = "{avg_trip_score}";') == []:
            
            add_record = f""" INSERT INTO trips (driver_id, do_you_like, style, condition, behaviour, avg_trip_score) VALUES (
                            "{driver_id}", "{do_you_like}", "{style_score}", "{condition_score}", "{behaviour_score}", "{avg_trip_score}"
                            );"""
            run_query(add_record)
    else:
        output = sqlite3_check()
        return output        
def main():
    driver_id = 3
    print("Did you enjoy the ride? (yes/no)\nIf you need more info about driver, write \"info\"")

    while True:
        user_input = input()
      
        if user_input == "no":
            do_you_like = 5
            print("Ouch, this is bad... So on a 1-10 scale, how would you rate the driving style of the driver?")
            while True:
                try:
                    style_score	 = int(input())
                except ValueError:
                    print("Oops! There is an error. Please try again!")
                    continue
                if style_score > 0 and style_score < 11:
                    print("Mhm... On a 1-10 scale, how would you rate the condition of the car?")
                    while True:
                        try:
                            condition_score = int(input())
                        except ValueError:
                            print("Oops! There is an error. Please try again!")
                            continue
                        if condition_score > 0 and condition_score < 11:
                            print("Okay, so on a 1-10 scale, how would you rate the behaviour of the driver?")
                            while True:
                                try:
                                    behaviour_score = int(input())
                                except ValueError:
                                    print("Oops! There is an error. Please try again!")

                                if behaviour_score > 0 and behaviour_score < 11:
                                    rate_list = [do_you_like, style_score, condition_score, behaviour_score]
                                    '''Take average from data input and round it'''
                                    avg_trip_score = round(mean(rate_list + 0.5))
                                    print(driver_id, do_you_like, style_score, condition_score, behaviour_score, avg_trip_score)
                                    trips(do_you_like, condition_score, style_score, behaviour_score, driver_id, avg_trip_score)
                                    break
                                else:
                                    print("The rating is in the wrong range, please try again!4")
                                    break
                        else:       
                            print("The rating is in the wrong range, please try again!3")
                            break
                else:       
                    print("The rating is in the wrong range, please try again!2")
                    break
  
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
                                    rate_list = [do_you_like, style_score, condition_score, behaviour_score]
                                    '''Take average from data input and round it'''
                                    avg_trip_score = round(mean(rate_list))
                                    print(driver_id, do_you_like, style_score, condition_score, behaviour_score, avg_trip_score)
                                    trips(do_you_like, condition_score, style_score, behaviour_score, driver_id, avg_trip_score)

                                    break
                                else:
                                    print("The rating is in the wrong range, please try again!4")
                        else:       
                            print("The rating is in the wrong range, please try again!3")
                else:       
                    print("The rating is in the wrong range, please try again!2")


        elif user_input == "info":
            print("Information about your driver:")
            name = remove_sym(str(run_query(f'SELECT name FROM drivers WHERE id = "{driver_id}"')))
            family_name = remove_sym(str(run_query(f'SELECT family_name FROM drivers WHERE id = "{driver_id}"')))
            print("Name: " + name + " " + family_name)
            car_plate = remove_sym(str(run_query(f'SELECT plate_number FROM drivers WHERE id = "{driver_id}"')))
            print("Driver\'s car plate number: " + car_plate)
            avg_score = remove_sym(str(run_query(f"SELECT AVG(avg_trip_score) FROM trips WHERE driver_id = {driver_id};")))
            print("Driver\'s rating: " + avg_score +"/10")
        
        elif user_input == "test":
            print("Closing program...")
            break
        # elif user_input == "developer_mode":
        #     print("You entered into a developer\'s mode, choose a right setting:\n")
        #     print("Write \"add\", to add new driver into a database")
        #     print("Write \"change_id\" to change program\'s current driver_id")
        #     while True:
        #         user_input = input()
        #         if user_input == "add":
        #             print("Passed!")
        #         elif user_input == "change_id":
        #             print("Passed!")

        else:
            print("Try Again1")
    # driver_name = 'Amed'
    # driver_family_name = 'Hame'
    # driver_plate_number = '125 ABC'
    # driver(driver_name, driver_family_name, driver_plate_number)
    print("I escaped!")
if __name__ == "__main__":
    main()

