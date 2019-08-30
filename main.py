import CircuitSolver as cs
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def main():
    test = cs.circuitSolver()
    equations = []
    Aw = a0/(1+s/w)
    
    equations.append(((Vi-Vp)/r3)-Vp/r4)
    equations.append((Vo-Vm)/r2-(Vm/r1))
    equations.append(Vo - Aw*(Vp-Vm))

    unknowns = [Vi,Vo,Vp]
    test.setEquations(equations)
    test.setUnknowns(unknowns)
    test.solveCircuit()
    H = test.getH()
    inpCurr = (test.getUnknowns()[Vi]-test.getUnknowns()[Vp]) / r3
    test.calcZinp(inpCurr)
    unknowns = [Vi,Vo,Vm]
    test.setUnknowns(unknowns)
    test.solveCircuit()
    outCurr = (test.getUnknowns()[Vo]-test.getUnknowns()[Vm]) / r2
    test.calcZout(outCurr)
    mod = simplify(sqrt(re(H)**2+im(H)**2))
    mod = mod.subs(s,I*2*p*f)
    print(latex(slewRate(H,SR,Vi,f)))

init_printing()
a0 = Symbol('a0',real = True, positive = True)
r1 = Symbol('R1',real = True, positive = True)
r2 = Symbol('R2',real = True, positive = True)
r3 = Symbol('R3',real = True, positive = True)
r4 = Symbol('R4',real = True, positive = True)
w = Symbol('W',real = True, positive = True)
f = Symbol('f',real = True, positive = True)
Vi = Symbol('Vi',real = True, positive = True)
Vo = Symbol('Vo',real = True, positive = True)
Vp = Symbol('Vp',real = True, positive = True)
Vm = Symbol('Vm',real = True, positive = True)
Vcc = Symbol('Vcc',real = True, positive = True)
SR = Symbol('SR',real = True, positive = True)
s = Symbol('s')
p = Symbol('pi',real = True, positive = True) 
#s = I*2*pi*f
main()