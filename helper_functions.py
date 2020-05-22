def printMonthlyData(title,month_data,net):
  print("Month of",title,":")
  print("=============")
  for log in month_data:
    printDailyData(log)
  print("Net sum for the month:",net)

def printDailyData(log):
  print(log.get_date() + ": " + str(log.get_calories_burned())+ " calories burned.")
  print("      "+str(log.get_calories_consumed())+" calories consumed.")
  print("Net:  "+str(log.get_calories_net())+" calories.")

def calculateMonthlyAvgNet(monthly_data):
  sum_net = 0 
  for day in monthly_data:
    sum_net += day.get_calories_net()
  return round(sum_net/len(monthly_data))