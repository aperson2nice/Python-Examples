# Sheila Robles
# Final Exam Summer 2016
# Python Version 3.0.1

import tkinter as tk
import DBUpdater
from tkinter import messagebox

score_track = tk.Tk()

def add_team_new(name):
    """Used with the modify_command in add team pane
        Args:
    name: the name of the team to add
            """
    messagebox.showinfo("Team Modified", "Team was successfully added")
    DBUpdater.addTeam([name,0,0,0,0])

def add_team_command():
    """Command used to add a team after being provided a name in the text entry"""
    add_team = tk.Tk()
    tk.Label(add_team, text="Enter Team Name").grid(row=0)
    name_entry = tk.Entry(add_team, text="Team Name")
    name_entry.grid(row=0, column=1, sticky="W")
    submit = tk.Button(add_team, text="Add a Team", command=lambda:add_team_new(name_entry.get()))
    submit.grid(row=1, column=1, sticky="W")


def update_information(name, comp, score):
    """Used with the modify_command in update_information command when submit is clicked"""
    messagebox.showinfo("Team Modified", "Team was successfully modified")
    DBUpdater.updateScore(name, comp, score)

def modify_command():
    """The modify window used to get information from the user as to what to modify"""
    modify_team = tk.Tk()

    tk.Label(modify_team, text="Enter Team Name").grid(row=0)
    tk.Label(modify_team, text="Enter Competition").grid(row=1)
    tk.Label(modify_team, text="Enter New Score").grid(row=2)

    name_entry = tk.Entry(modify_team, text="Team Name")
    name_entry.grid(row=0, column=1, sticky="W")
    comp_entry = tk.Entry(modify_team, text="Enter Competition Name")
    comp_entry.grid(row=1, column=1, sticky="W")
    score_entry = tk.Entry(modify_team, text="Enter the new score")
    score_entry.grid(row=2, column=1, sticky="W")
    submit = tk.Button(modify_team, text="Add/Modify Score", command=lambda:
                update_information(name_entry.get(),
                                   comp_entry.get(),
                                   score_entry.get()))
    submit.grid(row=3, column=1, sticky="W")



def initializer():
    """ use to initialize the app """
    frame = tk.Frame(score_track)
    frame.pack()

    button_frame = tk.Frame(score_track, height="200")
    button_frame.pack(side="top")

    add_team_button = tk.Button(button_frame, text="Add a Team", command=lambda: add_team_command())
    add_team_button.pack(side="top")
    add_score_button = tk.Button(button_frame, text="Add/Modify a score", command=lambda: modify_command())
    add_score_button.pack(side="bottom")
    view_hs_button = tk.Button(button_frame, text="View High Scores", command=lambda: DBUpdater.displayHighScore())
    view_hs_button.pack(side="bottom")

    score_track.mainloop()

initializer()

