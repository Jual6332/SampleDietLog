from Daylog_class import DayLog

# Initialisation
april_2020 = []

# Define April Data
current_rmr = 1982 # Resting metabolic rate

# Individual Logs 1-3
log1, log2, log3 = DayLog(), DayLog(), DayLog()
log1.set_date("4/19")
log1.set_calories_burned(current_rmr)
log1.set_calories_consumed(960*2+90)
log1.add_exercise(170)

log2.set_date("4/21")
log2.set_calories_burned(current_rmr)
log2.set_calories_consumed(2220)
log2.add_exercise(295+159)

# Store Data 
april_2020.append(log1)
april_2020.append(log2)
#april_2020.append(DayLog("4/27",295+1982,1655))