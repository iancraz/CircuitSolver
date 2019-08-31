import CircuitSolver as cs
import StringParser as sp
import numpy as np
import matplotlib.pyplot as plt
import sympy as sy
import tkinter as tk


def main():
    sy.init_printing()
    stringParser = sp.stringParser()
    circuit = cs.circuitSolver()
    window = tk.Tk()
    window.title("Circuit Solver")
    window.geometry('600x400')
    txt = tk.Entry(window,width=20)
    txt.grid(column=3, row=1)
    txt.focus()
    btn = tk.Button(window, text="Set Equation", command=lambda : clicked(txt.get(),stringParser))
    btn.grid(column=3, row=2)
    btn2 = tk.Button(window, text="Calculate", command=lambda : calculate(stringParser,circuit))
    btn2.grid(column=3, row=3)
    window.mainloop()

def clicked(string,stParser):
    stParser.decode(string)
    return
def calculate(stParser, circuitSolver):
    circuitSolver.setEquations(stParser.getExpressionList())
    circuitSolver.setUnknowns()
    circuitSolver.solveCircuit()
    print(circuitSolver.getH())
    return
main()