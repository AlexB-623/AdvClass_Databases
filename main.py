import sqlite3

def create_table():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""CREATE TABLE "Seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
);
""")
    connection.commit()
    connection.close()

#("A1", "0", "90"), ("A2", "1", "100"), ("A3", "0", "80")
def insert_record():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    INSERT INTO "Seat" (seat_id, taken, price) VALUES ("A4", "0", "90")
    """)
    connection.commit()
    connection.close()

#insert_record()

def select_all():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM Seat
    """)
    result = cursor.fetchall()
    connection.close()
    return result

# print(select_all())

def select_specific_columns():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM Seat
    """)
    result = cursor.fetchall()
    connection.close()
    return result

# print(select_specific_columns())

def select_conditional():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT "seat_id", "price" FROM Seat WHERE "price">89
    """)
    result = cursor.fetchall()
    connection.close()
    return result

# print(select_conditional())

def update_value():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    UPDATE "Seat" SET "taken" = "1" WHERE "seat_id" = "A3"
    """)
    connection.commit()
    connection.close()

#update_value()

def delete_record():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    DELETE FROM "Seat" WHERE "seat_id" = "A3"
    """)
    connection.commit()
    connection.close()

# delete_record()

def dynamic_update_value(occupied, seat_id):
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    UPDATE "Seat" SET "taken" = ? WHERE "seat_id" = ?
    """, [occupied, seat_id])
    connection.commit()
    connection.close()

dynamic_update_value(occupied=0, seat_id="A2")