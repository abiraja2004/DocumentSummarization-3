from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, LpInteger, \
    LpAffineExpression

if __name__ == "__main__":
    #LpMaximize means maximize the objective
    problem = LpProblem("counting to seven", LpMaximize)

    objects = {"stele" : (20, 400),
               "codex" : (10, 3000),
               "manuscript" : (5, 2900),
               "tablet" : (3, 50),
               "slab" : (2, 10),
               "plaque" : (8, 150) }

    extraConstraint1 = False
    extraConstraint2 = False

    varTab = {}
    for obj in objects:
        varTab[obj] = LpVariable(obj, 0, 1, LpInteger)

    #the first line added to the problem is the objective
    objective = []
    for obj, (wt, chs) in objects.items():
        objective.append( (varTab[obj], chs) )
    problem += LpAffineExpression(objective)

    constraint = []
    for obj, (wt, chs) in objects.items():
        constraint.append( (varTab[obj], wt) )
    problem += ( LpAffineExpression(constraint) <= 25)

    if extraConstraint1:
        problem += varTab["manuscript"] + varTab["codex"] <= 1

    if extraConstraint2:
        problem += varTab["codex"] <= varTab["tablet"]

    #solve the problem...
    problem.solve()

    #check that this worked
    print ("Problem status:", LpStatus[problem.status])

    #access information about the solution
    chs = 0
    wt = 0
    for varName, val in varTab.items():
        print ("Took", varName, "?", val.varValue)
        if val.varValue:
            (objWt, objChs) = objects[varName]
            chs += objChs
            wt += objWt

    print("Total characters", chs)
    print ("Total weight", wt)
