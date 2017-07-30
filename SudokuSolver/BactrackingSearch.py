#--------------------INSIDE SOLVING FUNCTION------------------------
def Select_Unassigned_Variables(assigned_values):
    global character_list
    for i in range(16):
        if set(assigned_values)[i] != set(character_list)[i] and assigned_values[i] != "-":
            unassigned_values += [character_list[i]]
    return unassigned_values    

def BacktrackingSearch(dict, plist):
    original_list = plist
    for item in solution_list:
        for x in range(len(solution_list)):
            for y in range(len(solution_list)):
                if plist[x][y] == "-":
                    plist[x][y] = item
                    return Bactrack(x,y,plist, original_list)
    return Backtrack(x, y, plist, original_list)
    
def Backtrack(x, y, assignment, plist):
    if is_complete(x,y,assignment):
        return assignment
    guess = Select_Unassigned_Variables(plist)
    for value in solution_list:
        if
'''
def Backtrack(x, y, assignment, plist):
    if is_complete(x,y,assignment):
        return assignment
    guess = Select_Unassigned_Variables(plist)
    for value in solution_list:
        if

def Backtracking-Search(csp) returns a solution or failure
    return Backtrack({}, csp)
def Backtrack(assignment, csp) returs a solution or failure
    if assignment is complete then return assignment
    var <--- Select-Unassigned-Variable(csp)
    for each value in Order-Domain-Values(var,assignment,csp) do
        if value is consistent with assignment then
            add{var = value} to assignment
            inferences <-- Inference(csp, var, value)
            if != failure then
                add inferences to assignment
                result <-- Backtrack(assignment, csp)
                if result != failure then
                    return result
            remove {var = value} and inferences from assingment
    return failure
'''