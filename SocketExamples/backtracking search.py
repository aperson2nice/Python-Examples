def Backtracking-Search(csp):
    # returns a solution or failure
    return Backtrack({}, csp)
        
def Backtrack(assignment, csp):
    # returns a solution or failure
    if isComplete(assignment):
        return assignment
    variable = select_unassigned_variables(csp)
    for value in Order_Domain_Values(variable, assignment, csp):
        if isConsistent(value, assignment):
            addToAssignment(variable) #add{var=value} to assignment
            inferences = Inference(csp, variable, value)
            if inferences != failure:
                addToAssignment(inferences)
                result = Backtrack(assignment, csp)
                if result != failure:
                    return result
        removeFromAssignment(var = value, inferences)
    return failure
    