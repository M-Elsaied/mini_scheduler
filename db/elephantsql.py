import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Function to connect to the PostgreSQL database
def get_connection():
    return psycopg2.connect(os.getenv('ELEPHANTSQL_URL'))

# Function to initialize the database schema
def init_db():
    with get_connection() as conn:
        with conn.cursor() as cur:
            create_tables(cur)
        conn.commit()

# Function to create tables
def create_tables(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS services (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        duration INTERVAL NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS providers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        schedule JSON NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id SERIAL PRIMARY KEY,
        service_id INT REFERENCES services(id),
        provider_id INT REFERENCES providers(id),
        start_time TIMESTAMP WITH TIME ZONE NOT NULL,
        end_time TIMESTAMP WITH TIME ZONE NOT NULL,
        UNIQUE(service_id, provider_id, start_time)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS waitlists (
        id SERIAL PRIMARY KEY,
        service_id INT REFERENCES services(id),
        provider_id INT REFERENCES providers(id),
        user_name VARCHAR(100) NOT NULL,
        requested_time TIMESTAMP WITH TIME ZONE NOT NULL
    );
    """)

if __name__ == '__main__':
    init_db()
