# Main Script
# Goal: Calculate Monthly net caloric difference per year 
# Drawback: Limited personal data
from helper_functions import *

#from MonthlyData2020.April_data import april_2020
#from MonthlyData2020.May_data import may_2020

# Initialization of empty monthly data
august_2020, september_2020 = [], []
october_2020, november_2020, december_2020 = [], [], []

# Calculate average net caloric difference per month
april_avg_net = calculateMonthlyAvgNet(april_2020)
may_avg_net = calculateMonthlyAvgNet(may_2020)

# Display Data for the user
# 1. Display data by month
# 2. Display more recent data first
printMonthlyData("May",may_2020,may_avg_net)
print("\n")
printMonthlyData("April",april_2020,april_avg_net)