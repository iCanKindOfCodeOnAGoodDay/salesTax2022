# Online Python - IDE, Editor, Compiler, Interpreter
# Feb 23, 2026 | Scott Quashen

# Shopify Sales Tax 2022 - Estimator based on missing data
# 7 sales of 13 accounted for; 1/7 is located in California | missing ~ 50% of the data
# Sales of unknown origin will be multiplied by 1/7th ratio estimating portion of revenue sales-taxable by Caifornia

# Data
# Payouts include up to 2 sales
payoutsQuarterEndingSep30 = [96.5, 145.05, 33.68, 63.69, 31.74, 38.54, 69.31, 101.65, 28.83]
payoutsQuarterEndingDec31 = [141.33]

# definitions
def total(payment):
    total = 0
    for month in payment:
        total += month
    return total

# function calls
salesSep = total(payoutsQuarterEndingSep30)
salesDec = total(payoutsQuarterEndingDec31)

###################################################################################################
# variables #################################

# September Quarter | No known sales to California customers
caRatio = 1/7 # details in header
otherState = 33.68 + 63.39 + 31.74 + 38.54 + 101.65 + 28.83
unknown = salesSep - otherState # subtract the one known ca sale
calEstimated = unknown * caRatio
estimatedOutOfState = salesSep - calEstimated
caTax = calEstimated * .1 # due to uknown sales total, we'll use the established ratio on remaining amount
print("\n#\nQuarter ending September 30\n")
print(f"Sales:                                              {salesSep:.2f}")
print(f"Known out of state:                                 {otherState:.2f}")
print(f"Uknown sales:                                       {unknown:.2f}")
print(f"Ratio adjusted out of state estimation:             {estimatedOutOfState:.2f}")
print()
print("Ratio of sales to Cal customers:                    1/7")
print(f"California taxable sales estimation:                {calEstimated:.2f} out of {estimatedOutOfState:.2f}")
print(f"Estimated ca sales tax:                             {caTax:.2f}")
inventoryPersonallyUsed = 90
taxOnPersonals = inventoryPersonallyUsed * .1
combinedSepTax = caTax + taxOnPersonals
print()
print("Inventory kept for personal use in quarter:         90")
print(f"Additional tax due to personal usage:               {taxOnPersonals:.2f}")
print("_________________________________________________________________________\n")
print(f"Sales tax due:                                              {combinedSepTax:.2f}")


# Decemeber Quarter | 1 of 1 sale is to California Customer
salesTaxDec = salesDec * .1
print("\n\n#\nQuarter ending December 31                          1/1 Sale in California\n")
print(f"Sales:                                              {salesDec:.2f}")
print("_________________________________________________________________________\n")
print(f"Sales tax due:                                              {salesTaxDec:.2f}")
print("\n\n\n#")

#Actual Total
totalSales = salesSep + salesDec
actualTotalTax = combinedSepTax + salesTaxDec
estimatedTax = totalSales * .1
print("Totals\n")
print(f"Total Sales:                                        {totalSales:.2f}")
print(f"Estimated Tax:                                      {estimatedTax:.2f}")
print("_________________________________________________________________________\n")
print(f"Actual Total Tax:                                           {actualTotalTax:.2f}")
print("\n\n\nEND")

