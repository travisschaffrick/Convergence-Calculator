from sympy import *
import matplotlib.pyplot as plt

init_printing()
x, y, z, a, b, n = symbols('x y z a b n')

def render(function, full_equation, variable):
    answer = r'f(x) = ' + latex(full_equation)
    limit = latex(Limit(full_equation, x, oo)) + " = " + str(limit(full_equation, x, oo))
    ax=plt.subplot(111)
    ax.text(0.05,0.4,r"$%s$" %(answer),fontsize=30,color="black") #modified fx
    ax.text(0.05,0.1,r"$%s$" %(limit),fontsize=30,color="black") #limit
    plt.show()


def nth_term(function, variable):
    ans = limit(function, x, oo)
    if (ans != 0):
        return ("Diverges as nth term != 0")
    return ("nth term divergence test inconclusive")

# print(nth_term_test((3*x**2)/(x**2), 'x'))


def ratio(function, variable):
    # calculating
    fx = function
    fx_1 = function.replace(x, x+1)
    full_equation = simplify(Abs(fx_1/fx))

    # rendering
    render(function, full_equation, x)
    return "limit as x-> inf = " + str(limit(full_equation, x, oo))

# print(ratio((x*2**(x)*factorial((x+1))/(3**(x)*factorial(x))),'x'))

def p_series(function, variable):
    function = simplify(function)
    n,d = fraction(function)

    function /= n
    n = n - n.subs(x, 0)
    function *= n

    function = simplify(function)
    n,d = fraction(function)

    function *= d
    d = d - d.subs(x, 0)
    function /= d

    function = simplify(function)
    if (n.is_constant()):
        if (d.as_base_exp()[1] > 1):
            print("Converges by p-series, p = " + str(d.as_base_exp()[1]))
        elif (d.as_base_exp()[1] <= 1):
            print("Diverges by p-series, p = " + str(d.as_base_exp()[1]))

p_series((3*x+2)/(x*(x+1)),'x')