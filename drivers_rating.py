from sqlite3_helper import sqlite3_create, sqlite3_run
import os
import re
sqlite3_file = 'drivers.sqlite3'
sqlite3_drivers_schema = 'drivers.sql'
sqlite3_trips_schema = 'trips.sql'
sqlite3_file_trips = 'trips.sqlite3'
from statistics import mean
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def negative_review(driver_id):
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
                            avg_trip_score = round(mean(rate_list))
                            trips(do_you_like, condition_score, style_score, behaviour_score, driver_id, avg_trip_score)
                            print("Thanks for you review! Closing program...")
                            exit()
                        else:
                            print("The rating is in the wrong range, please try again!")
                            break
                else:       
                    print("The rating is in the wrong range, please try again!")
                    break
        else:       
            print("The rating is in the wrong range, please try again!")
            break

def dev_mode_new_driver():
    print("Enter driver\'s name:")
    d_name = input()
    print("Enter driver\'s family name:")
    df_name = input()
    print("Enter driver car\'s plate number:")
    plt_number = input()
    print(f"New car driver\'s name is {d_name} {df_name}, and his/her car plate number is {plt_number}")
    print("This is correct? (y/n)")
    while True:
        user_input = input()
        if user_input == "y":
            print("Writing data to database...\n\n\n\n\n\n\n\n")
            driver(d_name, df_name, plt_number)
            return_developer_mode()
            break
        elif user_input == "n":
            print("Aborting operation...\n\n\n\n\n\n\n\n")
            return_developer_mode()
            break
        else:
            print("Error, please try again")

def dev_exit():
    print("Exiting from developer\'s mode...\n\n\n\n\n\n\n\n\n")
    print("Did you enjoy the ride? (yes/no)\nIf you need more info about driver, type \"info\"\nIf you need close the program, type \"exit\"")

def positive_review(driver_id):
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
                            trips(do_you_like, condition_score, style_score, behaviour_score, driver_id, avg_trip_score)
                            print("Thanks for you review! Closing program...")
                            exit()
                        else:
                            print("The rating is in the wrong range, please try again!")
                else:       
                    print("The rating is in the wrong range, please try again!")
        else:       
            print("The rating is in the wrong range, please try again!")
            
def return_developer_mode():
    print("You entered into a developer\'s mode, choose a right setting:\n")
    print("Type \"add\", to add new driver into a database")
    print("Type \"change_id\" to change program\'s current driver_id")
    print("Type \"exit\" to exit from developer\'s mode")

def remove_sym(name):
    name = re.sub(r"[\[\]]",'',name)
    name = name.strip("()")
    name = name.replace("'", "")
    name = name.replace(",", "")
    return name

def program_exit():
    print("Closing program...")

def dev_change_id(driver_id):
    print(f"Current driver_id is {driver_id}")
    print("Do you want to change this value? (y/n)")
    while True:
        user_input = input()
        if user_input == "y":
            print("Enter value:")
            new_id = int(input())
            print("Changing value...")
            driver_id = new_id
            print(f"Operation completed successfully!\nNew driver_id is {driver_id}")
            print("Information about selected driver:")
            name = remove_sym(str(run_query(f'SELECT name FROM drivers WHERE id = "{driver_id}"')))
            family_name = remove_sym(str(run_query(f'SELECT family_name FROM drivers WHERE id = "{driver_id}"')))
            print("Name: " + name + " " + family_name)
            car_plate = remove_sym(str(run_query(f'SELECT plate_number FROM drivers WHERE id = "{driver_id}"')))
            print("Driver\'s car plate number: " + car_plate)
            trip_amount = remove_sym(str(run_query(f'SELECT COUNT(driver_id) FROM trips WHERE driver_id = "{driver_id}"')))
            print(f"Number of trips: {trip_amount}")
            print("Returning back to developer menu...\n\n\n")

            return_developer_mode()
            return driver_id

        elif user_input == "n":
            print("Aborting operation...\n\n\n\n\n\n\n\n")
            return_developer_mode()
            break
        else:
            print("Error")

def driver_info(driver_id):
    print("Information about your driver:")
    name = remove_sym(str(run_query(f'SELECT name FROM drivers WHERE id = "{driver_id}"')))
    family_name = remove_sym(str(run_query(f'SELECT family_name FROM drivers WHERE id = "{driver_id}"')))
    print("Name: " + name + " " + family_name)
    car_plate = remove_sym(str(run_query(f'SELECT plate_number FROM drivers WHERE id = "{driver_id}"')))
    print("Driver\'s car plate number: " + car_plate)
    avg_score = remove_sym(str(run_query(f"SELECT AVG(avg_trip_score) FROM trips WHERE driver_id = {driver_id};")))
    avg_score = round(float(avg_score), 1)
    if avg_score < 5.9:
        avg_score_colored = colored(225, 0, 0, str(avg_score))
        avg_score_colored = avg_score_colored.replace(" ", "")
    elif avg_score > 5.9 and avg_score < 7.9:
        avg_score_colored = colored(255, 191, 0, str(avg_score))
        avg_score_colored = avg_score_colored.replace(" ", "")
    elif avg_score < 8:
        avg_score_colored = colored(0, 132, 80, str(avg_score))
        avg_score_colored = avg_score_colored.replace(" ", "")
    print("Driver\'s rating: " + avg_score_colored +"/10")
    trip_amount = remove_sym(str(run_query(f'SELECT COUNT(driver_id) FROM trips WHERE driver_id = "{driver_id}"')))
    print(f"Number of trips: {trip_amount}")
    print("End of information list...\n\n\n\n")
    print("Did you enjoy the ride? (yes/no)\nIf you need more info about driver, type \"info\"\nIf you need close the program, type \"exit\"")

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

def dev_mode_activate():
    while True:
        user_input = input()
        if user_input == "add":
            dev_mode_new_driver()

        elif user_input == "change_id":
            driver_id = dev_change_id(driver_id)

        elif (user_input == "exit"):
            dev_exit()
            break
        else:
            print("Error")
                    
def main():
    driver_id = 3
    print("Did you enjoy the ride? (yes/no)\nIf you need more info about driver, type \"info\"\nIf you need close the program, type \"exit\"")

    while True:
        user_input = input()
      
        if user_input == "no":
            negative_review(driver_id)
  
        elif user_input == "yes":
            positive_review(driver_id)

        elif user_input == "info":
            driver_info(driver_id)

        elif user_input == "exit":
            program_exit()
            return driver_id

        elif user_input == "developer_mode":
            return_developer_mode()
            while True:
                user_input = input()
                if user_input == "add":
                    dev_mode_new_driver()

                elif user_input == "change_id":
                    driver_id = dev_change_id(driver_id)

                elif (user_input == "exit"):
                    dev_exit()
                    break
                elif (user_input == "search"):
                    print("Please enter driver\'s name:")
                    search_name = input()
                    print("Please enter driver\'s family name:")
                    search_fname = input()
                    print("Please enter driver car\' car table number:")
                    search_tnumber = input()
                    print("Gimme sec...")


                else:
                    print("Error")        
        else:
            print("Try Again")
    # driver_name = 'Amed'
    # driver_family_name = 'Hame'
    # driver_plate_number = '125 ABC'
    # driver(driver_name, driver_family_name, driver_plate_number)
if __name__ == "__main__":
    main()

