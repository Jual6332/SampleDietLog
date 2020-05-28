from helper_functions import *

from MonthlyData2020.April_data import april_2020
from MonthlyData2020.May_data import may_2020

# Initialisation
august_2020, september_2020 = [], []
october_2020, november_2020, december_2020 = [], [], []

# Calculate Average Net per Month
may_avg_net = calculateMonthlyAvgNet(may_2020)
april_avg_net = calculateMonthlyAvgNet(april_2020)

# Display Data per Month
printMonthlyData("May",may_2020,may_avg_net)
print("\n")
printMonthlyData("April",april_2020,april_avg_net)