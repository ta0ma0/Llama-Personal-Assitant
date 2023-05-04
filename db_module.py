import sqlite3


def write_to_db(data_list):
    # Create table if it does not exist
    conn = sqlite3.connect('data/questions_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions_data
                  (id INTEGER PRIMARY KEY, date DATE, question TEXT, answer 
                  TEXT, comment TEXT)''')
    sql = f"INSERT INTO questions_data (date, question, answer) VALUES \
    ('{data_list[0]}', '{data_list[1]}', '{data_list[2]}')"
    conn.execute(sql)
    conn.commit()
