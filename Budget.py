#Pay/budget calculator. Enter which pay it is, then see upcoming bills and amount left over, plus see how much should be going to
# savings etc.

#All bills due during the first pay of the month.
houseInsurance = 105.48 #4th
carInsurance = 139.25 #16th
carPayment = 558.48 #5th
bankingFee = 4.0 #6th
mortgage = 658.3 #7th
tfsa1 = 200.0 #5th
toSavings1 = 100.0 #5th

#All bills due during the second pay of the month.
appleOne = 21.79 #20th
rogers = 219.61 #20th
netflix = 24.14 #20th
propertyTax = 91.46 #20th
#need to add input for NB Power
studentLoan = 166.67 #EOM
tfsa2 = 200.0 #20th
toSavings2 = 900.0 #20th

payNum = input("Is this the first pay of the month? ")
payAmount = input("How much was the pay? ")


def budget(payNum):
    if payNum == "yes":
        moneyLeft = float(payAmount) - houseInsurance - carInsurance - carPayment - bankingFee - mortgage - tfsa1 - toSavings1
        print("House insurace $"+ str(houseInsurance) + " on the 4th")
        print("Car Insurance $" + str(carInsurance) + "o n the 16th.")
        print("Car Payment $" + str(carPayment) + " on the 5th")
        print("Banking fee $" + str(bankingFee) + " on the 6th")
        print("Mortgage $" + str(mortgage) + " on the 7th")
        print("TFSA $" + str(tfsa1) + " on the 5th")
        print("To Savings $" + str(toSavings1) + "on the 5th")
        print("Money left = $" + str(moneyLeft))
        extraSavings = moneyLeft - 500 
        print("Kepp $500 in chequeing and move $" + str(extraSavings) + "to savings")
    else:
        powerBill = input("How much was the powerbill? ")
        moneyLeft = float(payAmount) - appleOne - rogers - netflix - propertyTax - studentLoan - tfsa2 - toSavings2 - float(powerBill)
        print("Apple One $" + str(appleOne) + " on the 20th")
        print("Rogers $" + str(rogers) + " on the 20th")
        print("Netflix $"+ str(netflix) + " on the 20th")
        print("Property Tax $" + str(propertyTax) + " on the 20th")
        print("Student Loan $" + str(studentLoan) + " on the last day of the month")
        print("TFSA $" + str(tfsa2) + " on the 20th")
        print("To Savings $" + str(toSavings2) + " on the 20th")
        extraSavings = moneyLeft - 500 
        print("Kepp $500 in chequeing and move $" + str(extraSavings) + " to savings")

budget(payNum)











