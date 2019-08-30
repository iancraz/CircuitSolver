import CircuitSolver as cs
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import math


def main():
    sy.init_printing()
    a0 = sy.Symbol('a0',real = True, positive = True)
    r1 = sy.Symbol('R1',real = True, positive = True)
    r2 = sy.Symbol('R2',real = True, positive = True)
    r3 = sy.Symbol('R3',real = True, positive = True)
    r4 = sy.Symbol('R4',real = True, positive = True)
    w = sy.Symbol('W',real = True, positive = True)
    f = sy.Symbol('f',real = True, positive = True)
    Vi = sy.Symbol('Vi',real = True, positive = True)
    Vo = sy.Symbol('Vo',real = True, positive = True)
    Vm = sy.Symbol('Vm',real = True, positive = True)
    s = sy.Symbol('s') 
    i1 = sy.Symbol('I1',real = True) 
    i2 = sy.Symbol('I2',real = True) 
    i3 = sy.Symbol('I3',real = True) 
    i4 = sy.Symbol('I4',real = True) 
    i5 = sy.Symbol('I5',real = True) 
    Iinp = sy.Symbol('Iinp',real = True)
    Iout = sy.Symbol('Iout',real = True)

    
    test = cs.circuitSolver()
    equations = []
    Aw = a0/(1+s/w)
    
    equations.append(Iinp-i2-i3)
    equations.append((Vi-Vm)/r1 -Iinp)
    equations.append(Vm/r3-i2)
    equations.append(Vo- Aw*(-Vm))
    equations.append((Vm-Vo)/r2 -i3)
    equations.append(Iout-i3-i5)
    equations.append(Vo/r4 - i5)
    unknowns = [Vi,Vo,Iinp, Iout, Vm, i3, i5]

    test.setEquations(equations)
    test.setUnknowns(unknowns)
    test.solveCircuit(Vi,Vo,Iinp,Iout)
    test.changeToFreq()
    print(test.getH())

main()