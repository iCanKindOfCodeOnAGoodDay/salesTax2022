
# Online Python - IDE, Editor, Compiler, Interpreter

# Feb 23, 2026 | Scott Quashen
# Shopify Sales Tax 2022 - Estimator based on missing data
# 7 sales of 13 accounted for; 1/7 is located in California | missing ~ 50% of the data

# payout data (payments have 1 or 2 sales | mostly 1) 
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

# Totals
###
totalSales = salesSep + salesDec
estimatedTax = totalSales * .1
print(f"Total Sales:                                        {totalSales:.2f}")
print(f"Estimated tax:                                      {estimatedTax:.2f}\n")

# September | No known california sales
###

caRatio = 1/7 # this is the ratio we will use to apply based on known sales data of ~50% sample
otherState = 33.68 + 63.39 + 31.74 + 38.54 + 101.65 + 28.83
unknown = salesSep - otherState # subtract the one known ca sale
calEstimated = unknown * caRatio
estimatedOutOfState = salesSep - calEstimated
caTax = calEstimated * .1 # due to uknown sales total, we'll use the established ratio on remaining amount

print("Quarter ending September 30")
print("Ratio of sales attributed to california: 1/7th")


print(f"Sales:                                              {salesSep:.2f}")
print(f"Known out of state:                                 {otherState:.2f}")
print(f"Uknown sales:                                       {unknown:.2f}")
print(f"Estimated out of state based on 6/7 ratio:          {estimatedOutOfState:.2f}")
print(f"California taxable sales estimation:                {calEstimated:.2f}")
print(f"Estimated ca sales tax:                             {caTax:.2f}")

# Decemeber Quarter | 1 of 1 sale is CA 
###

salesTaxDec = salesDec * .1

print("\nQuarter ending December 31")
print("All orders from california")
print(f"Sales:                                      {salesDec:.2f}")
print(f"Sales tax due:                              {salesTaxDec:.2f}")

# Actual Total
# actualTotalTax = caTax + salesTaxDec
# print(f"\nActual total tax | both quarters:           {actualTotalTax:.2f}")
