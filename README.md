# 🎮 ETL — Pokémon Database

A Python-based ETL (Extract, Transform, Load) pipeline that scrapes Pokémon stats from [PokémonDB](https://pokemondb.net/pokedex/all), structures the data, and loads it into a PostgreSQL database.

---

## 📁 Repository Structure

```
ETL---pokemon-database/
│
├── pokemon_scraper.py        # ETL pipeline script
└── pokemon_data.csv          # Extracted dataset
```

---

## ⚙️ ETL Pipeline

### Extract
- Sends an HTTP request to the [PokémonDB Pokédex](https://pokemondb.net/pokedex/all)
- Parses the full Pokédex HTML table using BeautifulSoup

### Transform
- Parses each row to retrieve number, name, type(s), and base stats
- Dual-type Pokémon have their types joined into a single comma-separated string (e.g. `Fire, Flying`)
- Stores all records in a Pandas DataFrame before loading

### Load
- Connects to a local PostgreSQL database via psycopg2
- Creates the `pokemon` table if it does not already exist
- Inserts all records row by row and commits the transaction

---

## 📊 Database Schema

**Table: `pokemon`**

| Column | Type | Description |
|---|---|---|
| `number` | VARCHAR(10) | Pokédex number |
| `name` | VARCHAR(100) | Pokémon name |
| `type` | VARCHAR(100) | Type(s), comma-separated for dual types |
| `total` | INT | Sum of all base stats |
| `hp` | INT | HP |
| `attack` | INT | Attack |
| `defense` | INT | Defense |
| `sp_atk` | INT | Special Attack |
| `sp_def` | INT | Special Defense |
| `speed` | INT | Speed |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- PostgreSQL with a database named `pokemon_db`

### Install Dependencies

```bash
pip install requests beautifulsoup4 pandas psycopg2
```

### Configure Database Credentials

Open `pokemon_scraper.py` and update the connection details:

```python
db_host = 'localhost'
db_port = '5432'
db_name = 'pokemon_db'
db_user = 'postgres'
db_password = 'your_password'
```

### Run the Script

```bash
python pokemon_scraper.py
```

On success, the terminal will print:
```
Data successfully scraped and stored in the database!
```

---

## 🛠️ Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-43B02A?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

- **Requests** — HTTP requests to fetch the webpage
- **BeautifulSoup4** — HTML parsing and data extraction
- **Pandas** — In-memory data structuring before load
- **psycopg2** — PostgreSQL database connection and insertion
- **PostgreSQL** — Database storage

---

## 📄 Data Source

[PokémonDB — Full Pokédex](https://pokemondb.net/pokedex/all)

---

## 👤 Author

**Roy** — [GitHub](https://github.com/RJT28)
