import requests
import psycopg2
from psycopg2 import extras

DB_CONFIG = {
    "host": "localhost",
    "database" : "pokewiki",
    "user" : "zago",
    "password" : "secretpassword",
    "port" : "5432"

}

def insert_types():

    print ("Trying to insert Types")

    try:

        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connection with PostgreSQL made with sucess.")

        for type_number in range(1,19):

            response = requests.get(f"https://pokeapi.co/api/v2/type/{type_number}")

            if response.status_code == 200:
                
                data = response.json()

                sql = """INSERT INTO type(type_id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (type_id) DO NOTHING;
                    """

                valores = (data['id'], data['name'])

                cursor.execute(sql, valores)
                print (f"Insert: {data['name']} ID {data['id']}")

                connection.commit()

    except Exception as e:
        
        print(f"Error in connection", e)

def insert_abilitys():
     
    print ("Trying to insert Abilitys")

    try:

        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connection with PostgreSQL made with sucess.")

        for ability_number in range(1,308):

            response = requests.get(f"https://pokeapi.co/api/v2/ability/{ability_number}")

            if response.status_code == 200:
                
                data = response.json()

                sql = """INSERT INTO ability(ability_id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (ability_id) DO NOTHING;
                    """

                valores = (data['id'], data['name'])

                cursor.execute(sql, valores)
                print (f"Insert: {data['name']} ID {data['id']}")

                connection.commit()

    except Exception as e:
        
        print("Error in connection",e)

def insert_egg_group():
     
    print ("Trying to insert Egg Groups")

    try:

        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connection with PostgreSQL made with sucess.")

        for egg_group_number in range(1,17):

            response = requests.get(f"https://pokeapi.co/api/v2/egg-group/{egg_group_number}")

            if response.status_code == 200:
                
                data = response.json()

                sql = """INSERT INTO egg_group(egg_group_id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (egg_group_id) DO NOTHING;
                    """

                valores = (data['id'], data['name'])

                cursor.execute(sql, valores)
                print (f"Insert: {data['name']} ID {data['id']}")

                connection.commit()

    except Exception as e:
        
        print("Error in connection",e)

def insert_generations():
     
    print ("Trying to insert Generations")

    try:

        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connection with PostgreSQL made with sucess.")

        for generation_number in range(1,10):

            response = requests.get(f"https://pokeapi.co/api/v2/generations/{generation_number}")

            if response.status_code == 200:
                
                data = response.json()

                sql = """INSERT INTO generation(generation_id, name)
                        VALUES (%s, %s)
                        ON CONFLICT (generation_id) DO NOTHING;
                    """

                valores = (data['id'], data['name'])

                cursor.execute(sql, valores)
                print (f"Insert: {data['name']} ID {data['id']}")

                connection.commit()

    except Exception as e:
        
        print("Error in connection",e)

def insert_pokemons():

    print ("Trying to insert Generations")

    try:

        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        print("Connection with PostgreSQL made with sucess.")

        for pokemon_number in range(1,1026):

            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}")

            if response.status_code == 200:

                data = response.json()

                sql = """INSERT INTO pokemon(pokemon_id, pokemon_num, name, height, weight)
                        VALUES (%s, %s, %s, %s, %s)

                        ON CONFLICT (pokemon_id) DO NOTHING;
                    """

                valores = (data['id'], data['id'], data['name'], data['height'], data['weight'])

                cursor.execute(sql, valores)
                print (f"Insert: {data['name']} ID {data['id']} NUM {data['id']} HEIGHT {data['height']} WEIGHT {data['weight']}")

                connection.commit()


    except Exception as e:
        
        print("Error in connection",e)

insert_types()
insert_abilitys()
insert_egg_group()
insert_generations()
insert_pokemons()