#function that calcalates monthly tax
def monthly_tax(ann_inc): 
#checks if income belongs to tax bracket, calculates monthly tax
    if ann_inc <= 250000: 
        mon_tax = 0
        return mon_tax
    elif ann_inc > 250000 and ann_inc <= 400000: 
        mon_tax = ((ann_inc - 250000) * 0.15) / 12
        return mon_tax
    elif ann_inc > 400000 and ann_inc <= 800000: 
        mon_tax = (22500 + (ann_inc - 400000) * 0.2) / 12
        return mon_tax  
    elif ann_inc > 800000 and ann_inc <= 2000000: 
        mon_tax = (102500 + (ann_inc - 800000) * 0.25) / 12
        return mon_tax     
    elif ann_inc > 2000000 and ann_inc <= 8000000: 
        mon_tax = (402500 + (ann_inc - 2000000) * 0.3) /12
        return mon_tax
    else:
        mon_tax = (2202500 + (ann_inc - 8000000) * 0.35) /12
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
monthlyTax = monthly_tax(annualIncome)
annualTax = annual_tax(annualIncome)

#outputs monthly and annual tax
print("\nYour monthly tax is PHP {:.2f}.".format(monthlyTax))
print("Your annual tax is PHP {:.2f}.".format(annualTax))
