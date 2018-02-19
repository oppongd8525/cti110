#CTI-110
#P2TI - Sales Prediction
#Desmond Oppong
#0215018
#Program to estimate annual profit of a company
#


#Input company total sales for the whole year.

totalSales = float(input("Enter company yearly sales. "))

#Calculating annual progfit made for the whole year.

annualProfit = 0.23 * totalSales                   
                     
print("Company profit is. $ ", format(annualProfit,'.2f'))
