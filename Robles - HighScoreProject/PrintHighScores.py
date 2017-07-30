# Sheila Robles
# Final Exam Summer 2016
# Python Version 3.0.1

""" This py file will format the output of a list containing name and overall
    scores of the highest performing teams.
"""
import ViewHighscore

def sort_highscores(list_of_scores):
    """ Sort a list of tuples containing team name and overall score
        Args:
            list_of_scores: list of tuples with team name and high score
    """
    new_list = []
    new_item = ("none",0)
    while(len(list_of_scores) != 0):
        for tpl in list_of_scores:
            if tpl[1] >= new_item[1]:
                new_item = tpl
        new_list += [new_item]
        list_of_scores.remove(new_item)
        new_item=("", 0)
    return new_list


def format_teamname(name):
    """ return a formatted name so as to maintain a centered appearance with 13 chars
            Args:
                name: name to format.
    """
    while len(name) != 13:
        if len(name) >= 13:
            name = name[:13]
        else:
            name = " " + name + " "
    return name


def formatDisplay(teams_info):
    """ return a formatted high score display
                Args:
                    team_info: list of tuples with name and overall score of teams
    """
    string_output = "-----------------------------\n" +\
                    "---------- OVERALL ----------\n" +\
                    "--Place-----Team------Score--\n" +\
                    "-----------------------------\n"
    place = 1
    team_info_list = sort_highscores(teams_info)
    for team_info in team_info_list:
        name, score = team_info
        name = format_teamname(name)
        string_output += ("-  " + str(place) + " - {0} - {1} -\n".format(name, score))
        place += 1

    string_output += "-----------------------------\n"

    ViewHighscore.update_view(string_output.format(tuple(team_info_list)))

