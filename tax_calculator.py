#function that calcalates monthly tax
def monthly_tax(mon_inc): 
#checks if income belongs to tax bracket, calculates monthly tax
    if mon_inc <= 20833: 
        mon_tax = 0
        return mon_tax
    elif mon_inc > 20833 and mon_inc <= 33332: 
        mon_tax = (mon_inc - 20833) * 0.15
        return mon_tax
    elif mon_inc >= 33333 and mon_inc <= 66666: 
        mon_tax = 1875 + (mon_inc - 33333) * 0.2
        return mon_tax  
    elif mon_inc >= 66667 and mon_inc <= 166666: 
        mon_tax = 8541.8 + (mon_inc - 66667) * 0.25
        return mon_tax     
    elif mon_inc >= 166667 and mon_inc <= 666666: 
        mon_tax = 33541.8 + (mon_inc - 166667) * 0.3
        return mon_tax
    else:
        mon_tax = 183541.8 + (mon_inc - 666667) * 0.35
        return mon_tax 
  
#function that calculates annual tax  
def annual_tax(ann_inc): 
#checks if income belongs to tax bracket, calculates annual tax
    if ann_inc <= 250000: 
        ann_tax = 0
        return ann_tax
    elif ann_inc > 250000 and ann_inc <= 400000: 
        ann_tax = (ann_inc - 250000) * 0.15
        return ann_tax
    elif ann_inc > 400000 and ann_inc <= 800000: 
        ann_tax = 22500 + (ann_inc - 400000) * 0.2
        return ann_tax  
    elif ann_inc > 800000 and ann_inc <= 2000000: 
        ann_tax = 102500 + (ann_inc - 800000) * 0.25
        return ann_tax     
    elif ann_inc > 2000000 and ann_inc <= 8000000: 
        ann_tax = 402500 + (ann_inc - 2000000) * 0.3
        return ann_tax
    else:
        ann_tax = 2202500 + (ann_inc - 8000000) * 0.35
        return ann_tax 

#asks user for monthly income
monthlyIncome = float(input("Enter your monthly income: "))

#calculate annual income 
annualIncome = monthlyIncome * 12

#calls functions
monthlyTax = monthly_tax(monthlyIncome)
annualTax = annual_tax(annualIncome)

#outputs monthly and annual tax
print("\nYour monthly tax is PHP {:.2f}.".format(monthlyTax))
print("Your annual tax is PHP {:.2f}.".format(annualTax))
