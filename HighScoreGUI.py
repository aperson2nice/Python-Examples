# Sheila Robles
# Python v3.0.1

import tkinter as tk
from tkinter import messagebox

highscore_root = tk.Tk()

team_name_selector_variable = tk.StringVar()
team_name_selector_variable.set("none")

def view_high_score():
    high_score_view = tk.Tk()

def are_you_sure_you_want_to_add():
    messagebox.showwarning("Warning", "Are you sure you want to add a new team?")


def add_team_message(team):
    messagebox.showinfo("Success", "Team {0} was successfully added.".format(team))


def add_score_message(team):
    messagebox.showinfo("Hooray", "New score was added to team {0}.".format(team))


def select_team_name(lbl):
    lbl.configure(text=team_name_selector_variable.get())



def initialize():
    # All instances of widget_app are of the global and not a local reference
    global highscore_root

    highscore_root.title("High Score Tracker")





    # --------Button Frame-------------
    button_frame = tk.Frame(highscore_root)
    #button_frame_label = tk.Label(button_frame, text="Select and option from below.")
    #button_frame_label.grid(row=0, column=0, columnspan=3)
    #add_team_button = tk.Button(button_frame, text="Add Team", command=add_team_message("TEAM TEST"))
    #add_score_button = tk.Button(button_frame, text="Add/Update Score", command=add_score_message())
    #add_team_button.grid(row=1, column=0)
    #add_score_button.grid(row=1, column=1)
    #button3.grid(row=1, column=2)
    #button4.grid(row=2, column=1)
    button_frame.grid(row=0, column=0)
#
#
#     # ---------------------Entry Frame-------------------------------
#     entry_frame = tk.Frame(highscore_root)
#     entry_frame_label = tk.Label(entry_frame, text="Entry Widget")
#     entry_frame_label.pack()
#     entry = tk.Entry(entry_frame)
#     entry_btn = tk.Button(entry_frame, text="Click",
#                           command=lambda: messagebox.showinfo("Entry", entry.get()))
#     entry.pack()
#     entry_btn.pack()
#     entry_frame.grid(row=1, column=0)
#
#     # ---------------------Radio Buttons Frame--------------------------
#     rb_frame = tk.Frame(highscore_root)
#     rb_frame_label = tk.Label(rb_frame, text="Radio Buttons Widget")
#     rb_frame_label.grid(row=0, column=0, columnspan=2)
#     rb_selection_label = tk.Label(rb_frame, text="You selected:")
#     rb_selection = tk.Label(rb_frame, textvariable=radio_button_group_variable, width=10)
#
#     eggs_rb = tk.Radiobutton(rb_frame, text="Eggs",
#                              variable=radio_button_group_variable, value="eggs")
#     spam_rb = tk.Radiobutton(rb_frame, text="Spam",
#                              variable=radio_button_group_variable, value="spam")
#     elder_rb = tk.Radiobutton(rb_frame, text="Elder Berries",
#                               variable=radio_button_group_variable, value="elder berries")
#     eggs_rb.grid(row=1, column=0, columnspan=2, sticky="w")
#     spam_rb.grid(row=2, column=0, columnspan=2, sticky="w")
#     elder_rb.grid(row=3, column=0, columnspan=2, stick="w")
#     rb_selection_label.grid(row=4, column=0)
#     rb_selection.grid(row=4, column=1)
#     rb_frame.grid(row=1, column=2)
#
#     # ----------------Text Frame-------------------------------
#     text_frame = tk.Frame(highscore_root, width=200, height=200)
#     text_frame.pack_propagate(False)
#     text_frame_label = tk.Label(text_frame, text="Text Widget")
#     text_frame_label.pack()
#     text = tk.Text(text_frame, bg="black", fg="green", insertbackground="white")
#     text.insert(tk.INSERT, "Hello.....")
#     text.insert(tk.END, "Bye Bye.....")
#     text.pack()
#     text_frame.grid(row=2, column=1)

    highscore_root.mainloop()


initialize()



