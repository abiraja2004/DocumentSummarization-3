from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, LpInteger,\
    LpAffineExpression

if __name__ == "__main__":
    #define an equation defined by c1x1 + c2x2 ... cnxn
    coefficients = [2, 4, -5, 1]

    #build an empty expression
    obj = LpAffineExpression()

    #add each var * coeff to the expression
    xis = []
    for ind, coeff in enumerate(coefficients):
        xi = LpVariable("x%d" % ind, 0, 10, LpInteger)
        #store the variables for later use (usually in constraints)
        xis.append(xi)
        obj += coeff * xi

    print "Equation:"
    print obj

    print "Variables:"
    print xis
