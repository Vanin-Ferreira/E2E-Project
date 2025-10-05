from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB", "testdb")
POSTGRES_USER = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")

@app.get("/")
def root():
    try:
        conn = psycopg2.connect(
            host=POSTGRES_HOST,
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD
        )
        conn.close()
        return {"status": "Connected to PostgreSQL!"}
    except Exception as e:
        return {"status": "Connection failed", "error": str(e)}