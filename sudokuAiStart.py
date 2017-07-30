list_of_needs = []

def set_list_of_needs(puzzle):
    global list_of_needs
    # set up in col, row
    list_of_needs += [puzzle]

def get_needed_spots(plist):
    for row in plst:
        for col in plst:
            if plst[col][row] == "-":
                set_list_of_needs((col,row))

def check needs()