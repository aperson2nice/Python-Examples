# Sheila Robles
# Final Exam Summer 2016
# Python Version 3.0.1

import tkinter as tk

def update_view(scores):
    """ Updates the view of the high score tk pane.
        Args:
            scores: a formatted strings with all the high score info to display
    """
    hsdisplay = tk.Tk()
    tk.Label(hsdisplay, text="Overall High Score Average").grid(row=0, column=0)

    overall_hs = tk.Text(hsdisplay, height=20, width=30)
    overall_hs.insert('insert',scores)
    overall_hs.grid(row=1, column=0)

    hsdisplay.mainloop()