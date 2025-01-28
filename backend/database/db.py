import sqlite3

DB_NAME = 'jobs.db'

# Create the db (if not exists) and jobs table in it
def setup_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            posted_date TEXT
        )
    ''')

    conn.commit() # Save the changes
    conn.close() # Close the connection

# Insert a new job into the db
def insert_job(job):
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO jobs (company, title, url, posted_date)
            VALUES (?, ?, ?, ?)
        ''', (job['company'], job['title'], job['url'], job['posted_date']))

        conn.commit()
    except sqlite3.IntegrityError:
        print(f"Job already exists: {job['url']}")
    finally:
        conn.close()

# Get all jobs from the db
def get_all_jobs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM jobs')
    jobs = cursor.fetchall()

    conn.close()

    return [{'id': row[0], 'company': row[1], 'title': row[2], 'url': row[3], 'posted_date': row[4]} for row in jobs]