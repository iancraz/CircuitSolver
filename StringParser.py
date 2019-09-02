import sympy as sy
from sympy import ask, Q, pi
from sympy.parsing.sympy_parser import (parse_expr , standard_transformations, implicit_multiplication)

class stringParser:
    def __init__(self):
        self.varList = []
        self.expressList = []
        self.unkownsList = []
        return
    
    def getVarList(self):
        return self.varList
    
    def decode(self,string):
        self.expressList.append(parse_expr(string,transformations=standard_transformations + (implicit_multiplication,)))
        temp = len(self.expressList)
        temp = list(self.expressList[temp-1].free_symbols)
        for i in range(0,len(temp)):
            for u in range(0,len(self.varList)):
                if temp[i] == self.varList[u][0].free_symbols:
                    self.expressList[len(self.expressList)-1].replace(temp[i],self.varList[u][1])


                    ##DEJE ACAAA
        for i in range(0,len(temp)):
            if temp[i] not in self.varList:
                self.varList.append(temp[i])
        return
    
    def setUnknowns(self,string):
        self.unkownsList = []
        temp = string.split(',')
        for i in range(0,len(temp)):
            temp1 = parse_expr(temp[i],transformations=standard_transformations + (implicit_multiplication,))
            self.unkownsList.append(list(temp1.free_symbols)[0])
        return
    
    def getUnknowns(self):
        return self.unkownsList
    
    def getExpressionList(self):
        return self.expressList

    def reset(self):
        self.varList = []
        self.expressList = []
        self.unkownsList = []
        return

    def eraseEq(self):
        self.expressList = []
        return

    def eraseUnk(self):
        self.unkownsList = []
        return

    def setImaginaryVariables(self,string):
        temp = string.split(',')
        for i in range(0,len(temp)):
            self.varList.append([temp[i],sy.Symbol(temp[i],complex = True)])
        return
    
    def setRealVariables(self,string,isPositive):
        temp = string.split(',')
        for i in range(0,len(temp)):
            if isPositive:
                self.varList.append([temp[i],sy.Symbol(temp[i],real = True, positive = True)])
            else:
                self.unkownsList.append([temp[i],sy.Symbol(temp[i],real = True)])
        return

    def eraseVariables(self):
        self.varList = []
        return