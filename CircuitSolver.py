# from sympy import Symbol
# from sympy import Function, simplify
# from sympy import init_printing
# from sympy.core.numbers import pi, I, oo
# from sympy.solvers.inequalities import solve_rational_inequalities
# from sympy.solvers.inequalities import reduce_rational_inequalities
# from sympy.solvers import solve
import sympy as sy
import numpy as np


class circuitSolver:
    def __init__(self):
        self.equations = None
        self.unknowns = None
        self.H = None
        self.zinp = None
        self.zout = None
        self.solution = []
        self.Vi = sy.Symbol('Vi', real=True)
        self.Vo = sy.Symbol('Vo', real=True)
        self.Iinp = sy.Symbol('Iinp', real=True)
        self.Iout = sy.Symbol('Iout', real=True, positive=True)
        self.s = sy.Symbol('s')
        self.f = sy.Symbol('f')
        self.mod = None
        self.phase = None
        self.resolveZinp = False
        self.resolveZout = False
        return

    def setEquations(self, equationsList):
        self.equations = equationsList
        return

    def setUnknowns(self, unknownsList):
        self.unknowns = unknownsList
        return

    def solveCircuit(self):
        self.solution = sy.solve(self.equations, self.unknowns, manual=1)
        if len(self.solution) != 0: 
            if type(self.solution) == list:
                temp = {}
                for i in range(0, len(self.solution[0])):
                    temp2 = self.solution[0]
                    temp[self.unknowns[i]] = temp2[i]
                self.solution = temp
            if len(self.solution) != 0:
                self.update()
        return

    def getH(self):
        return self.H

    def getMod(self):
        return self.mod

    def getPhase(self):
        return self.phase

    def getUnknowns(self):
        return self.solution

    def calcZinp(self, inpCurr):
        self.zinp = sy.simplify(self.solution[self.Vi] / inpCurr)
        return self.zinp

    def calcZout(self, outCurr):
        self.zout = sy.simplify(self.solution[self.Vo] / outCurr)
        return self.zout

    def getZinp(self):
        return self.zinp

    def getZout(self):
        return self.zout

    def reset(self):
        self.equations = None
        self.unknowns = None
        self.H = None
        self.zinp = None
        self.zout = None
        self.solution = None
        self.resolveZinp = False
        self.resolveZout = False
        return

    def update(self):
        if len(self.solution) != 0: 
            self.H = self.solution[self.unknowns[0]] / self.solution[self.unknowns[1]]
            self.H = sy.simplify(self.H)
            self.mod = sy.sqrt(sy.re(self.H) ** 2 + sy.im(self.H) ** 2)
            self.phase = sy.atan(sy.im(self.H) / sy.re(self.H)) * 180 / 3.14195
            if self.resolveZinp:
                self.zinp = self.solution[self.unknowns[1]] / self.solution[self.unknowns[2]]
            if self.resolveZout:
                self.zout = self.solution[self.unknowns[0]] / self.solution[self.unknowns[3]]
        # self.zinp = sy.simplify(self.zinp)
        return

    def changeToFreq(self):
        self.mod = self.mod.subs(self.s, sy.I * 2 * sy.pi * self.f)
        self.phase = self.phase.subs(self.s, sy.I * 2 * sy.pi * self.f)
        self.H = self.H.subs(self.s, sy.I * 2 * sy.pi * self.f)
        self.H = sy.simplify(self.H)
        self.mod = sy.simplify(self.mod)
        self.phase = sy.simplify(self.phase)
        return

    def resZinp(self):
        self.resolveZinp = True

    def resZout(self):
        self.resolveZout = True