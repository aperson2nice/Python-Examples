# Sheila Robles
# Final Exam Summer 2016
# Python Version 3.0.1

import sqlite3
import PrintHighScores

# constant fields available to DBUpdater
result_string = "Team: {0} | Auto: {1} | RC: {2} | Spirit: {3} | Video: {4}"
database_file = "score_tracker.db"

def team_exists(team):
    """Check database to see if team exists
        Args:
            team: the name of a team.
        Returns:
            boolean representing whether or not team exists.
    """
    exists = False
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        team_names = cursor.execute("""SELECT lower(teamname) FROM scores""")
        for row in team_names.fetchall():
            if row[0] == team.lower():
                exists = True
    return exists

def addTeam(teaminfo):
    """ Add a new team and it's info if it's not a current team
        Args:
            teaminfo: list containing name, and 4 competition scores
    """
    team, auto, rc_comp, spirit_comp, video_comp = teaminfo
    if team_exists(team): # Team already exists
        print("Team", team, "already exists.")
    else:
        with sqlite3.connect(database_file) as conn:
            #(teamname TEXT, autonomous TEXT, rc TEXT, spirit INT, video INT)
            conn.execute("INSERT INTO scores(teamname, autonomous, rc, spirit, video)\
            VALUES('{0}', '{1}', '{2}', '{3}', '{4}');".format(team, auto, rc_comp, spirit_comp, video_comp))

def updateScore(team, competition, newscore):
    """ Update a specific competition score for a team
            Args:
                teaminfo: list containing name, and 4 competition scores
                competition: name of the competition - autonomous, rc, spirit, video
                newscore: int value for new score
        """
    if team_exists(team):
        with sqlite3.connect(database_file) as conn:
            conn.execute("UPDATE scores SET {0} = '{1}'\
            WHERE teamname = '{2}';".format(competition, newscore, team))
    else:
        print("Invalid team name")

def getScores():
    """ Get all scores from database
            Return:
                list of tuples containing team neam and overall score
        """
    results = ""
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        team_scores = cursor.execute(""" SELECT * FROM scores;""")

        for row in team_scores.fetchall():
            teamname, auto, rc, spirit, video = row
            results += result_string.format(teamname, auto, rc, spirit, video) + "\n"
    return results

def displayHighScore():
    """ Display high scores from database
    """
    compiled_scores = []
    all_scores = getScores()
    for row in all_scores.splitlines():
        compiled_scores += [(row.split()[1], int(row.split()[4])+int(row.split()[7])+
                int(row.split()[10])+int(row.split()[13]))]
        print(compiled_scores)
    PrintHighScores.formatDisplay(compiled_scores)


def getTeamInfo(team):
    """ Get all information about a team
                Return:
                    list containing a teams information
            """
    results = ""
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        print("SELECT * FROM scores WHERE teamname = '{0}';".format(team))
        team_info = cursor.execute("SELECT * FROM scores WHERE teamname = '{0}';".format(team))
        print(team_info.fetchall())
        for row in team_info.fetchall():
            teamname, auto, rc, spirit, video = row
            results += result_string.format(teamname, auto, rc, spirit, video) + "\n"
    return results

