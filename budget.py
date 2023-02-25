import pandas as pd
import datetime as dt

frequency = {'daily':1,'weekly':7,'monthly':30,'yearly':365}

expInit = ''
expList = []
incInit = ''
incList = []

class Expense:
    daily = ''
    weekly = ''
    monthly = ''
    yearly = ''

    def __init__(self,name,amt,freq):
        self.name = name
        self.amt = amt
        self.freq = freq
        self.total()
        

    def total(self):
        self.daily = self.amt / frequency[self.freq]
        self.weekly = self.daily * frequency["weekly"]
        self.monthly = self.daily * frequency["monthly"]
        self.yearly = self.daily * frequency["yearly"]
        print("Yearly expense for ",self.name,"is " , self.yearly)

    

class Income:
    daily = ''
    weekly = ''
    monthly = ''
    yearly = ''

    def __init__(self,src,amt,freq):
        self.src = src
        self.amt = amt
        self.freq = freq
        self.total()

    def total(self):
        self.daily = self.amt / frequency[self.freq]
        self.weekly = self.daily * frequency["weekly"]
        self.monthly = self.daily * frequency["monthly"]
        self.yearly = self.daily * frequency["yearly"]
        print("Yearly income for ",self.src,"is " , self.yearly)

class Budget:
    def __init__(self,inc,exp,sav):
        self.income = inc
        self.exp = exp
        self.sav = sav

    def delegate(self):
        pass



def allExpense():
    df = pd.read_csv("expenses.csv")
    for index,row in df.iterrows():
        expInit = Expense(row[0],row[1],row[2])
        expList.append(expInit)

def allIncome():
    df = pd.read_csv("income.csv")
    for index,row in df.iterrows():
        incInit = Income(row[0],row[1],row[2])
        incList.append(incInit)

allIncome()

