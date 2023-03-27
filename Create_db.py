import os
import inspect
import sqlite3
from faker import Faker
from datetime import datetime

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    add_person_query = ""
    ('''
            CREATE THE TABLE IF DOES NOT EXISTS people (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                city TEXT NOT NULL,
                province TEXT NOT NULL,
                bio TEXT NOT NULL,
                age INTEGER NOT NULL,
                created_at DATETIME NOT NULL,
                updated_at DATETIME NOT NULL
            );
        ''')
    con.commit()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    fake = Faker()
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    for i in range(200):
            name = fake.name()
            email = fake.email()
            address = fake.address()
            city = fake.city()
            province = fake.province()
            bio = fake.bio()
            age = fake.random_int(min=1, max=100)
            created_at = datetime.now()
            updated_at = datetime.now()
        
            ('''
                INSERT INTO people (name, email,address,city,province,bio, age, created_at, updated_at) 
                
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                
            ''', (name, email,address,city,province,bio, age, created_at, updated_at))
    con.commit()

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__== '__main__':
    main()