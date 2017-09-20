# Not My Work, Example from School 
# Python v3.0.1

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

lbls = ["Button", "Canvas", "Checkbutton", "Entry",
        "Message", "Radiobuttons", "Scale", "Text", "Spinbox"]

highscore_root = tk.Tk()
    #doing_something = tk.BooleanVar()  # Used for checkbutton frame
team_name_selector_variable = tk.StringVar() # radio action button
team_name_selector_variable.set("none")
    #vert_scale_variable = tk.IntVar()
    #hori_scale_variable = tk.IntVar()

def message_dialog():
    messagebox.showinfo("Info", "I am an info box")


def wdialog():
    messagebox.showwarning("Warning", "Danger Will Robinson")


def edialog():
    messagebox.showerror("Error", "Windows has experienced an error...but" \
                                    " I'll never tell. :D")


def askq():
    res = messagebox.askyesno("Annoying", "Would you like to continue?")
    if res == False:
        res = messagebox.askquestion("Annoying", "Are you sure?")
        if "yes" in res:
            res = messagebox.askokcancel("Annoying", "This will close the app.")
            if res:
                while res:
                    res = messagebox.askretrycancel("Annoying", "Just kidding.")


    #def activate_checkbutton(lbl):
    #    if doing_something.get():
    #        lbl.configure(text="Did something")
    #    else:
    #        lbl.configure(text="Not doing something")


def select_team_name(lbl):
    lbl.configure(text=team_name_selector_variable.get())


def initialize():
    # All instances of widget_app are of the global and not a local reference
    global widget_app

    widget_app.title("Widgets!  Widgets Everywhere!")

    # --------Button Frame-------------
    button_frame = tk.Frame(widget_app)
    button_frame_label = tk.Label(button_frame, text="Button Widget")
    button_frame_label.grid(row=0, column=0, columnspan=3)
    button1 = tk.Button(button_frame, text="Show Message", command=mdialog)
    button2 = tk.Button(button_frame, text="Show Warning", command=wdialog)
    button3 = tk.Button(button_frame, text="Show Error", command=edialog)
    button4 = tk.Button(button_frame, text="Rabbit Hole", command=askq)
    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button4.grid(row=2, column=1)
    button_frame.grid(row=0, column=0)

    # ------------------Canvas Frame--------------
    canvas_frame = tk.Frame(widget_app)
    canvas_frame_label = tk.Label(canvas_frame, text="Canvas Widget")
    canvas_frame_label.pack()
    canvas = tk.Canvas(canvas_frame, width=80, height=80, bg="black")
    canvas.create_oval(5, 5, 80, 80, fill="yellow", activefill="green")
    canvas.create_oval(20, 20, 30, 30, fill="black")
    canvas.create_oval(50, 20, 60, 30, fill="black")
    canvas.create_arc(17, 20, 65, 70, start=180, extent=180, fill="red", activefill="blue")
    canvas.pack()
    canvas_frame.grid(row=0, column=1)

    # -------------------Checkbutton Frame------------------------
    check_button_frame = tk.Frame(widget_app)
    check_button_frame_label = tk.Label(check_button_frame, text="Checkbutton Widget")
    check_button_frame_label.grid(row=0, column=0, columnspan=2)
    do_something_lbl = tk.Label(check_button_frame, text="Not doing something")
    do_something_cb = tk.Checkbutton(check_button_frame, text="Something",
                                     onvalue=True, offvalue=False, variable=doing_something,
                                     command=lambda: activate_checkbutton(do_something_lbl))
    do_something_cb.grid(row=1, column=0, sticky="w")
    do_something_lbl.grid(row=1, column=1, sticky="e")
    check_button_frame.grid(row=0, column=2)

    # ---------------------Entry Frame-------------------------------
    entry_frame = tk.Frame(widget_app)
    entry_frame_label = tk.Label(entry_frame, text="Entry Widget")
    entry_frame_label.pack()
    entry = tk.Entry(entry_frame)
    entry_btn = tk.Button(entry_frame, text="Click",
                          command=lambda: messagebox.showinfo("Entry", entry.get()))
    entry.pack()
    entry_btn.pack()
    entry_frame.grid(row=1, column=0)

    # ---------------------Message Frame--------------------------------
    message_frame = tk.Frame(widget_app)
    message_frame_label = tk.Label(message_frame, text="Message Widget")
    message_frame_label.grid(row=0, column=0)
    msg = tk.Message(message_frame, relief=tk.RIDGE, borderwidth=4,
                     justify=tk.CENTER, text="I am nothing more than a glorified label.")
    msg.configure(font=("Courier New", 12))
    msg.grid(row=1, column=0)
    message_frame.grid(row=1, column=1)

    # ---------------------Radio Buttons Frame--------------------------
    rb_frame = tk.Frame(widget_app)
    rb_frame_label = tk.Label(rb_frame, text="Radio Buttons Widget")
    rb_frame_label.grid(row=0, column=0, columnspan=2)
    rb_selection_label = tk.Label(rb_frame, text="You selected:")
    rb_selection = tk.Label(rb_frame, textvariable=radio_button_group_variable, width=10)

    eggs_rb = tk.Radiobutton(rb_frame, text="Eggs",
                             variable=radio_button_group_variable, value="eggs")
    spam_rb = tk.Radiobutton(rb_frame, text="Spam",
                             variable=radio_button_group_variable, value="spam")
    elder_rb = tk.Radiobutton(rb_frame, text="Elder Berries",
                              variable=radio_button_group_variable, value="elder berries")
    eggs_rb.grid(row=1, column=0, columnspan=2, sticky="w")
    spam_rb.grid(row=2, column=0, columnspan=2, sticky="w")
    elder_rb.grid(row=3, column=0, columnspan=2, stick="w")
    rb_selection_label.grid(row=4, column=0)
    rb_selection.grid(row=4, column=1)
    rb_frame.grid(row=1, column=2)

    # -------------------Scale Frame----------------------------------
    scale_frame = tk.Frame(widget_app)
    scale_frame_label = tk.Label(scale_frame, text="Scale Widget")
    scale_frame_label.grid(row=0, column=0, columnspan=2)
    vert_scale = tk.Scale(scale_frame, from_=0, to=255, variable=vert_scale_variable)
    hori_scale = tk.Scale(scale_frame, from_=-180, to=180, orient=tk.HORIZONTAL, variable=hori_scale_variable)
    vert_lbl = tk.Label(scale_frame, textvariable=vert_scale_variable)
    hori_lbl = tk.Label(scale_frame, textvariable=hori_scale_variable)
    vert_scale.grid(row=1, column=0, columnspan=2)
    hori_scale.grid(row=2, column=0, columnspan=2)
    vert_lbl.grid(row=3, column=0)
    hori_lbl.grid(row=3, column=1)
    scale_frame.grid(row=2, column=0)

    # ----------------Text Frame-------------------------------
    text_frame = tk.Frame(widget_app, width=200, height=200)
    text_frame.pack_propagate(False)
    text_frame_label = tk.Label(text_frame, text="Text Widget")
    text_frame_label.pack()
    text = tk.Text(text_frame, bg="black", fg="green", insertbackground="white")
    text.insert(tk.INSERT, "Hello.....")
    text.insert(tk.END, "Bye Bye.....")
    text.pack()
    text_frame.grid(row=2, column=1)

    # ------------Spinbox---------------------------------------
    sb_frame = tk.Frame(widget_app)
    sb_frame_label = tk.Label(sb_frame, text="Spinbox Widget")
    sb_frame_label.pack()
    sb_variable = tk.IntVar()
    spinbox = tk.Spinbox(sb_frame, from_=0, to=10, wrap=True, textvariable=sb_variable)
    sb_lbl = tk.Label(sb_frame, textvariable=sb_variable)
    sb_lbl.pack()
    spinbox.pack()
    sb_frame.grid(row=2, column=2)

    widget_app.mainloop()


initialize()
