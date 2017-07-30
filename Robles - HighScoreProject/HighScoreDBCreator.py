# Sheila Robles
# Final Exam Summer 2016
# Python Version 3.0.1

import sqlite3

def create_db():
    """
        Used at the very beginning to create a sqlite3 database.
    """
    database_file = "score_tracker.db"
    with sqlite3.connect(database_file) as conn:
        conn.execute("""CREATE TABLE scores (teamname text, autonomous int, rc int, spirit int, video int);""")
        conn.execute("INSERT INTO scores(teamname, autonomous, rc, spirit, video)\
                    VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format("Default1",0,0,0,0))
        conn.execute("INSERT INTO scores(teamname, autonomous, rc, spirit, video)\
                            VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format("Default2", 0, 0, 0, 0))
        conn.execute("INSERT INTO scores(teamname, autonomous, rc, spirit, video)\
                                    VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format("Default3", 0, 0, 0, 0))
        conn.execute("INSERT INTO scores(teamname, autonomous, rc, spirit, video)\
                                    VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format("Default4", 0, 0, 0, 0))
        conn.execute("INSERT INTO scores(teamname, autonomous, rc, spirit, video)\
                                    VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format("Default5", 0, 0, 0, 0))

create_db()