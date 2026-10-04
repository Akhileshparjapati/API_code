import sqlite3

from fastapi import FastAPI

app= FastAPI()


con = sqlite3.connect("test.db",check_same_thread=False)

cursor=con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY,
    title text,
    complete text
    )
""")

con.commit()


@app.get("/")
def home():
    return {
        "message":"sqlite connected fine"
    }

