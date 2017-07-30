# Sheila Robles
# Final Exam Summer 2016
# Python Version 3.0.1

class Team(object):
    ''' A team with it's own dictionary of scores '''
    def __init__(self, team_name, team_members):
        self.team_name = team_name # name of team
        self.team_members = team_members # list of members
        self.scores = {"autonomous":[], "rc":[], "spirit":0, "video":0}
        
    def __str__(self):
        return "Team Name: " + str(self.team_name) + \
                "\nMembers: " + str(self.team_members) + \
                "\nScores: " + str(self.scores)

    def toList(self):
        return [self.team_name, str(self.scores["autonomous"]), str(self.scores["rc"]),
                self.scores["spirit"], self.scores["video"]]

    def addScore(self, score_type, score): # Later create an update score method
        if score_type == "spirit" or score_type == "video":
            self.scores == score
        else:
            self.scores[score_type] += score


if __name__ == "__main__":
    t1 = Team("Eastlake", ["Mary", "Anna", "Iris"])
    print(t1)

    t1.addScore("autonomous", [55])
    print(t1)    
    
    t1.addScore("autonomous", [13])
    print(t1)
    
    t1.addScore("rc", [13])
    print(t1)