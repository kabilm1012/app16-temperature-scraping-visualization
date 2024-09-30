import sqlite3

connection = sqlite3.connect("database.db")

def store(datetime, temp):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature VALUES(?,?)", [datetime, temp])
    connection.commit()

def read():
    cursor = connection.cursor()
    data = cursor.execute("SELECT * FROM temperature")
    data = data.fetchall()
    return data


if __name__ == "__main__":
    print(read())








