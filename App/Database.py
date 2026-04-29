import sqlite3

conn = sqlite3.connect("resume_analysis.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS analysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    job_description TEXT,
    score REAL
)
""")
conn.commit()


def save_analysis(filename, job_description, score):
    cursor.execute(
        "INSERT INTO analysis (filename, job_description, score) VALUES (?, ?, ?)",
        (filename, job_description, score)
    )
    conn.commit()
