"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
import sqlite3
import pandas as pd

def main():
    global db_path
    script_dir = get_script_dir()
    db_path = os.path.join(script_dir, 'social_network.db')

    # Get the names and ages of all old people
    old_people_list = get_old_people()

    # Print the names and ages of all old people
    print_name_and_age(old_people_list)

    # Save the names and ages of all old people to a CSV file
    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
  # Connect to the database
    con = sqlite3.connect(db_path)

    # Query the database for all people who are at least 50 years old
    cur = con.execute("SELECT name, age FROM people WHERE age >= 50")

    # Get the query results as a list of tuples
    old_people_list = cur.fetch_all()

    # Close the database connection
    con.close()

    # Return the list of old people
    return old_people_list

def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    for name, age in name_and_age_list:
        print(f"MR/MRS.{name} is {age} years old.")

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
 # Convert the list of tuples to a DataFrame
    df = pd.DataFrame(name_and_age_list, columns=["Name", "Age"])

    # Save the DataFrame to a CSV file
    df.to_csv(csv_path, header=False)

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(__file__)
    return os.path.dirname(script_path)
if __name__=='__main__':
    main()