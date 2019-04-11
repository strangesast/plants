import random
import time
import sqlite3

def generate(n = 60 * 60 * 24):
    data = [(int((random.random() * 12 + 15) * 100) / 100, random.randint(0, 512) + 512) for _ in range(n)]
    return data


if __name__ == '__main__':
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS recent
                 (time INTEGER, temp REAL, hum INTEGER)''')

    c.execute('''CREATE TABLE IF NOT EXISTS historical
                 (time INTEGER, avg_temp REAL, avg_hum INTEGER)''')

    t = int(time.time())
    temp = 15.5
    hum = 830
    c.execute('INSERT INTO recent VALUES (?, ?, ?)', (t, temp, hum))

    #data = generate()
    #print(data[0])

    conn.commit()
    conn.close()
