import sqlite3

database_file = 'shelf.db'
result_string = "Author: {0} | Title: {1} | Price: {2}"

with sqlite3.connect(database_file) as conn:
    cursor = conn.cursor()

    result_1 = cursor.execute(""" SELECT author,
    title, price FROM books WHERE price > 20;""")

    conn.execute("""UPDATE books SET price = 20
    WHERE price < 40;""")

    # getting user input
    #price_check = input("Price: ")
    #result_1 = conn.execute("SELECT author, title, price"
    #                        " FROM books WHERE price <= {};".format(
    #                        price_check))

    result_2 = cursor.execute("""SELECT * FROM books WHERE price >= 20""")

    for result in [result_1, result_2]:
        for row in result.fetchall():
            auth, title, price = row
            print(result_string.format(auth, title, price))
