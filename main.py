import matplotlib

class DayLog:
  def __init__(self,dat,burn,consum):
    self.date = dat;
    self.burned = burn;
    self.consumed = consum;

  def get_calories_burned(self):
    return self.burned;

  def get_calories_consumed(self):
    return self.consumed;

  def get_date(self):
    return self.date;

  def set_calories_burned(self,cals):
    self.burned = cals;

  def set_calories_consumed(self,cals):
    self.consumed = cals;

  def set_date(self,dat):
    self.date = dat;

# Initialisation
april_2020, may_2020, june_2020 = [], [], []
july_2020, august_2020, september_2020 = [], [], []
october_2020, november_2020, december_2020 = [], [], []

# Define April Data
april19 = DayLog("4/19",170,960*2+90)
april20 = DayLog("4/20",0,0)

april_2020.append(april19)
april_2020.append(april20)

# Display Data --- April
print("Calories Burned in April:")
print("=========================")
for log in april_2020:
  print(log.get_date() + ": " + str(log.get_calories_burned())+ " calories.")
print("\n")

# Display Data --- May
print("Calories Burned in April:")
print("=========================")