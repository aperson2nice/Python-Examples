import sqlite3

with sqlite3.connect('highscores.db') as conn:
    #Python 3 users, change raw_input to input.
    user = raw_input('Name: ')
    score = int(raw_input('Score: '))
    
    result = conn.execute("SELECT * FROM scores WHERE username=?", (user,))
    row = result.fetchone()
    
    #If the user does not exist then insert them into the table.
    if len(row) == 0:
        conn.execute("INSERT INTO scores(username, score) VALUES(?, ?)", (user,score))
    else:
        #If the user already exists then update their score if their new score is
        #greater than their current high score.
        if row[1] < score:
            conn.execute("UPDATE scores SET score=?", (score,))
        else:
            #Python 3 users, change print to function, print()
            print "Current high score for {} is {}".format(user, row[1])
    check_result = conn.execute("SELECT * FROM scores")
    for row in check_result.fetchall():
        #Python 3 users, change print to function, print()
        print row