import sympy as sy
from sympy import ask, Q, pi
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication)


class stringParser:
    def __init__(self):
        self.varList = []
        self.expressList = []
        self.unkownsList = []
        self.inpCurrent = None
        self.outCurrent = None
        return

    def getVarList(self):
        return self.varList

    def decode(self, string):
        self.expressList.append(
            parse_expr(string, transformations=standard_transformations + (implicit_multiplication,)))
        temp = len(self.expressList)
        temp = list(self.expressList[temp - 1].free_symbols)
        for i in range(0, len(temp)):
            check = False
            for u in range(0, len(self.varList)):
                temp2 = self.varList[u]
                temp2 = temp2[0]
                if str(temp[i]) == temp2:
                    temp2 = self.varList[u]
                    temp2 = temp2[1]
                    self.expressList[len(self.expressList) - 1] = self.expressList[len(self.expressList) - 1].subs(
                        temp[i], temp2)
                    check = True
                elif u == (len(self.varList) - 1) and check == False:
                    self.varList.append([str(temp[i]), temp[i]])
            if len(self.varList) == 0:
                self.varList.append([str(temp[i]), temp[i]])
        return

    def setUnknowns(self, string):
        # self.unkownsList = []
        temp = string.split(',')
        for i in range(0, len(temp)):
            temp1 = parse_expr(temp[i], transformations=standard_transformations + (implicit_multiplication,))
            temp1 = list(temp1.free_symbols)[0]
            check = False
            for u in range(0, len(self.varList)):
                temp2 = self.varList[u]
                if str(temp1) == temp2[0]:
                    self.unkownsList.append(temp2[1])
                    check = True
                elif u == (len(self.varList) - 1) and check == False:
                    self.unkownsList.append(temp1)

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

    def setImaginaryVariables(self, string):
        temp = string.split(',')
        for i in range(0, len(temp)):
            self.varList.append([temp[i], sy.Symbol(temp[i])])
        return

    def setRealVariables(self, string, isPositive):
        temp = string.split(',')
        for i in range(0, len(temp)):
            if isPositive:
                self.varList.append([temp[i], sy.Symbol(temp[i], real=True, positive=True)])
            else:
                self.varList.append([temp[i], sy.Symbol(temp[i], real=True)])
        return

    def eraseVariables(self):
        self.varList = []
        return

    def setCurrentEq(self, string, isInput):
        if isInput:
            var = sy.Symbol('Iinp')
            self.varList.append([str(var), var])
        else:
            var = sy.Symbol('Iout')
            self.varList.append([str(var), var])
        currentEq = parse_expr(string, transformations=standard_transformations + (implicit_multiplication,)) - var
        temp = list(currentEq.free_symbols)
        for i in range(0, len(temp)):
            check = False
            for u in range(0, len(self.varList)):
                temp2 = self.varList[u]
                temp2 = temp2[0]
                if str(temp[i]) == temp2:
                    temp2 = self.varList[u]
                    temp2 = temp2[1]
                    currentEq = currentEq.subs(temp[i], temp2)
                    check = True
                elif u == (len(self.varList) - 1) and check is False:
                    self.varList.append([str(temp[i]), temp[i]])
            if len(self.varList) == 0:
                self.varList.append([str(temp[i]), temp[i]])
        if isInput:
            self.inpCurrent = currentEq
            self.expressList.append(self.inpCurrent)
            self.varList.insert(2,[str(var),var])
            self.unkownsList.insert(2,var)
        else:
            self.outCurrent = currentEq
            self.expressList.append(self.outCurrent)
            self.varList.insert(3, [str(var),var])
            self.unkownsList.insert(3,var)
        return
