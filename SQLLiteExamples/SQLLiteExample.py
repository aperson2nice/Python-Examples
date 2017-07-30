import sqlite3

database_file = "shelf.db"

with sqlite3.connect(database_file) as conn:
    conn.execute("""CREATE TABLE books(author text,
                title text, price real);""")
    conn.execute("""INSERT INTO books(author, title, price)
                    VALUES('Jason Gregory', 'Game Engine Architecture', 57.55);""")
    conn.execute("""INSERT INTO books(author, title, price)
                    VALUES('JK Rowling', 'Harry Potter', 12.99);""")
    conn.execute("""INSERT INTO books(author, title, price)
                    VALUES('J.R.R Tolkien', 'The Hobbit', 10.63);""")
    conn.execute("""INSERT INTO books(author, title, price)
                    VALUES('Ernest Cline', 'Ready Player One', 12.99);""")



'''
sqlite_file = 'my_first_db.sqlite'    # name of the sqlite database file
table_name1 = 'my_table_1'  # name of the table to be created
table_name2 = 'my_table_2'  # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()'''