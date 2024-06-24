import numpy as np
import matplotlib as mp
import pandas as pd


class Metric(object):
    def __init__(tenor, limit, levelOne, levelTwo):
        int()
    def oneWeek(tenor):
        oneWeekliquidity = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = {3,5,7}, nrows = tenor)
        cLiquid = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = "Cumulative Liquidity")
        owL = float(oneWeekliquidity.sum())
        cL = float(cLiquid.sum())
        oneWeek = (owL / cL) * 100
        print(oneWeek)
    def oneMonth(tenor):
        oneMonthliquidity = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = {3,5,7}, nrows = tenor)
        cLiquid = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = "Cumulative Liquidity")
        omL = float(oneMonthliquidity.sum())
        cL = float(cLiquid.sum())
        oneMonth = (omL / cL) * 100
        print(oneMonth)
    def cumulativeLiquidity(tenor, limit):
        ()
    def liquidityRisk(tenor):
        liability = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = {9}, nrows = tenor)
        lR = float(tenor / liability)
        print(lR)
    def sourceReport(fundingLimit):
        {}
    def interentityLending(lendinglimit):
        ()
    def liquidityCoverage():
        lO = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = {8})
        lT = df.read_excel("BankTreasuryTest.xlsx", "Sheet1", index_col = {8})
        stress = Metric()
        st = stress.liquidityRisk(365)
        lC = float((lO + lT) / st) * 100
        if(lC < 100){
            print(100 - lC)
        }
        else(){
            print(lC - 100)
        }
