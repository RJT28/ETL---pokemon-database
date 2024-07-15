import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2

# Step 1: Scrape the Data

url = 'https://pokemondb.net/pokedex/all'
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', {'id': 'pokedex'})

# Extract column headers
headers = [header.text for header in table.find_all('th')]

# Extract rows
rows = []
for row in table.find('tbody').find_all('tr'):
    cols = row.find_all('td')
    number = cols[0].text.strip()
    name = cols[1].text.strip()
    types = [type.text.strip() for type in cols[2].find_all('a')]
    type_combined = ', '.join(types)
    total = int(cols[3].text.strip())
    hp = int(cols[4].text.strip())
    attack = int(cols[5].text.strip())
    defense = int(cols[6].text.strip())
    sp_atk = int(cols[7].text.strip())
    sp_def = int(cols[8].text.strip())
    speed = int(cols[9].text.strip())
    rows.append([number, name, type_combined, total, hp, attack, defense, sp_atk, sp_def, speed])

# Create a DataFrame
df = pd.DataFrame(rows, columns=['Number', 'Name', 'Type', 'Total', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed'])

# Step 2: Store Data in PostgreSQL

# Database connection details
db_host = 'localhost'
db_port = '5432'
db_name = 'pokemon_db'
db_user = 'postgres'
db_password = 'Your_password'

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
cur = conn.cursor()

# Create a table for the Pokémon data
create_table_query = '''
CREATE TABLE IF NOT EXISTS pokemon (
    number VARCHAR(10),
    name VARCHAR(100),
    type VARCHAR(100),
    total INT,
    hp INT,
    attack INT,
    defense INT,
    sp_atk INT,
    sp_def INT,
    speed INT
);
'''
cur.execute(create_table_query)
conn.commit()

# Insert data into the table
insert_query = '''
INSERT INTO pokemon (number, name, type, total, hp, attack, defense, sp_atk, sp_def, speed)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

for index, row in df.iterrows():
    cur.execute(insert_query, tuple(row))

# Commit the transaction
conn.commit()

# Close the connection
cur.close()
conn.close()

print("Data successfully scraped and stored in the database!")
